# Anime Recommendation System

This project is an Anime Recommendation System built using **Jupyter Notebook**, **Python**, and **scikit-learn** for the recommendation model. The system uses **content-based filtering** with **cosine similarity** to suggest anime based on user-selected preferences. It provides a simple UI using **Streamlit**, integrates an API to fetch and display currently popular anime titles.

## Features

- **Content-Based Filtering**: Recommendations are generated using cosine similarity based on user input.
- **User Input**: Users can select or input anime they want recommendations based on.
- **API Integration**: Fetches the most popular anime currently trending.
- **Streamlit UI**: A user-friendly interface to interact with the recommendation engine.


## Tech Stack

- **Programming Language**: Python
- **Libraries/Frameworks**:
  - [scikit-learn](https://scikit-learn.org/stable/): Machine learning library for building the recommendation engine.
  - [pandas](https://pandas.pydata.org/): For handling and processing the anime dataset.
  - [numpy](https://numpy.org/): For numerical operations.
  - [Streamlit](https://streamlit.io/): Framework for building the web app interface.
  - [Requests](https://docs.python-requests.org/en/master/): For making API calls.

## Installation

To run the project locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/anime-recommendation-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd anime-recommendation-system
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```


4. Run the application using Streamlit:
   ```bash
   streamlit run app.py
   ```
   
## Usage

Once the app is running, the UI will allow users to:

- Select or input anime titles they are interested in.
- Get personalized recommendations based on selected anime using content-based filtering.
- View currently trending anime fetched from an API.

## How it Works

1. **Content-Based Filtering**: The recommendation engine uses cosine similarity to match user-selected anime with similar tags.
2. **Model Creation**: The content-based filtering system is built using pandas, numpy, and scikit-learn.
3. **API Integration**: The app fetches the most popular anime titles using an API, updating the list in real-time.

## Project Structure

- `notebooks/`: Contains Jupyter notebooks used for developing and training the model.
- `app.py`: Streamlit app for running the UI.
- `model/`: Contains the saved model and data for recommendations.
- `requirements.txt`: List of dependencies needed to run the project.

![Main page](https://github.com/jhevtech/Anime-Recommendation-system/blob/main/images/animerecmain%20page.png)

![Result page](

## Future Enhancements

- Implement more sophisticated recommendation algorithms such as collaborative filteringo or a hybrid approach.
- Improve UI design and add additional filters.
- Expand the dataset to include more anime titles.



