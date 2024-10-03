import pickle
import streamlit as st
import requests


def fetch_poster(anime_id):
    url =

def recommend(anime):
    index = animes[animes['Name'] == anime].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True , key= lambda x: x[1])
    recommended_anime_name =[]
    recommended_anime_poster = []
    for i in distances[1:30]:
        anime_id = animes.iloc[i[0]]['anime_id']
        recommended_anime_poster.append(fetch_poster(anime_id))
        recommended_anime_name.append(animes.iloc[i[0]]Name)
    return recommended_anime_name, recommended_anime_poster

st.header("Anime Recommendation")
animes = pickle.load(open('models/anime_list.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))

anime_list = animes['Name'].values
selected_anime = st.selectbox(
    'Type or select an anime to get recommendations',
    anime_list
)

if st.button('Show Recommendation'):
    recommended_animes_name, recommended_anime_poster = recommend(selected_anime)