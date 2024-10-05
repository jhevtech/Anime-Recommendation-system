import pickle
import streamlit as st
import requests
import time

@st.cache_data
def fetch_poster(anime_id):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}"
    for _ in range(4):
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            description_path = data['data']['synopsis']
            genre_path = [genre['name'] for genre in data['data']['genres']]
            poster_path = data['data']['images']['jpg']['image_url']
            return description_path, genre_path, poster_path
        elif response.status_code == 429:
            st.warning("Rate limit reached. Retrying in 30 seconds.")
            time.sleep(30)
        else: 
            #st.error("Failed to fetch poster: "+ response.reason)
            return None, None, None
    
    st.error("Failed to fetch poster after multiple attempts.")
    return None, None, None

@st.cache_data
def get_top_anime():
    url = "https://api.jikan.moe/v4/top/anime"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        top_anime_list = []
        for anime in data['data'][:4]:
            top_anime_list.append({
                "name": anime['title'],
                "id": anime['mal_id'],
                "poster": anime['images']['jpg']['image_url'],
                "genre": [genre['name'] for genre in anime['genres']]
            })
        return top_anime_list
    else: 
        st.error("Failed to fetch top anime: " + response.reason)
        return[]

st.header("**Anime Recommendation**")
animes = pickle.load(open('models/anime_list.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))


top_anime = get_top_anime()

# display top animes
st.subheader("Top Anime")

cols = st.columns(4)
for col, anime in zip(cols, top_anime):
            with col:
                st.text(anime['name'])
                st.image(anime['poster'])
                st.text("Genres: " + ", ".join(anime['genre']))
                

#display recommended animes
def recommend(anime):
    index = animes[animes['Name'] == anime].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True , key= lambda x: x[1])
    recommended_anime_name =[]
    recommended_anime_poster = []
    recommended_anime_description =[]
    recommended_anime_genre =[]

    for i in distances[1:30]:
        anime_id = animes.iloc[i[0]].anime_id     
        description, genre, poster = fetch_poster(anime_id)

        if poster:     
            recommended_anime_poster.append(poster)
            recommended_anime_name.append(animes.iloc[i[0]].Name)
            recommended_anime_description.append(description if description else "No description available.")
            recommended_anime_genre.append(", ".join(genre) if genre else "No genres available.")
            
        time.sleep(1)
        if len(recommended_anime_poster) >= 4:
            break
        
    return recommended_anime_name, recommended_anime_poster, recommended_anime_description, recommended_anime_genre


anime_list = animes['Name'].values
selected_anime = st.selectbox(
    'Type or select an anime to get recommendations',
    anime_list
)


if st.button('Show Recommendation'):
    recommended_anime_name, recommended_anime_poster, recommended_anime_description, recommended_anime_genre = recommend(selected_anime)
    col1, col2, col3, col4= st.columns(4)
    
    for idx, col in enumerate([col1, col2, col3, col4]):
        if idx < len(recommended_anime_name):
            with col:
                st.subheader(recommended_anime_name[idx])
                st.image(recommended_anime_poster[idx])
                st.markdown("Genres: " + recommended_anime_genre[idx])
                st.markdown("Description: " + recommended_anime_description[idx])



