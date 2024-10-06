# Anime Recommendation System

This project is an Anime Recommendation System built using **Jupyter Notebook**, **Python**, and **scikit-learn** for the recommendation model. The system uses **content-based filtering** with **cosine similarity** to suggest anime based on user-selected preferences. It provides a simple UI using **Streamlit**, integrates an API to fetch and display currently popular anime titles, and is deployed on **Heroku**.

## Features

- **Content-Based Filtering**: Recommendations are generated using cosine similarity based on user input.
- **User Input**: Users can select or input anime they want recommendations based on.
- **API Integration**: Fetches the most popular anime currently trending.
- **Streamlit UI**: A user-friendly interface to interact with the recommendation engine.
- **Heroku Deployment**: Easily accessible from anywhere via a web interface.
- **AWS S3 Integration**: The `similarity.pkl` model is stored in AWS S3 for easy access due to its file size.


## Tech Stack

- **Programming Language**: Python
- **Libraries/Frameworks**:
  - [scikit-learn](https://scikit-learn.org/stable/): Machine learning library for building the recommendation engine.
  - [pandas](https://pandas.pydata.org/): For handling and processing the anime dataset.
  - [numpy](https://numpy.org/): For numerical operations.
  - [Streamlit](https://streamlit.io/): Framework for building the web app interface.
  - [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): AWS SDK for Python to interact with AWS S3.
  - [Requests](https://docs.python-requests.org/en/master/): For making API calls.
- **Deployment**: Heroku and AWS S3

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

4. Upload the similarity.pkl file to AWS S3 following the steps in the AWS S3 Setup section below.

5. Run the application using Streamlit:
   ```bash
   streamlit run app.py
   ```
   
## AWS S3 Setup

To handle the large similarity.pkl file that cannot be pushed to GitHub, follow these steps to store and retrieve it from AWS S3:

1. Upload the File to AWS S3:
- Sign in to AWS Management Console and navigate to S3.
- Create an S3 bucket if you don't have one.
- Upload the similarity.pkl file to your S3 bucket.
- Copy the file's object URL for later use.

2. Install boto3:
- In your local environment, install the boto3 library:
```bash
pip install boto3
```
- Update your requirements.txt to include boto3:
```bash
pip freeze > requirements.txt
```
3. Configure Heroku to Access AWS S3:
- In your Heroku environment, set the AWS credentials as environment variables:
```bash
heroku config:set AWS_ACCESS_KEY_ID=your_access_key
heroku config:set AWS_SECRET_ACCESS_KEY=your_secret_key
```
4. Modify app.py to Load the Model from S3: Update app.py to download the similarity.pkl file from AWS S3 using boto3:

```app.py
import boto3
import pickle

# AWS S3 client setup
s3 = boto3.client(
    's3',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)

bucket_name = 'your-bucket-name'
file_key = 'models/similarity.pkl'

# Download the model file from S3
s3.download_file(bucket_name, file_key, 'similarity.pkl')

# Load the model
similarity = pickle.load(open('similarity.pkl', 'rb'))
```
5. Deploy the Changes:
-Commit your changes and push them to Heroku:
```bash
git add .
git commit -m "Add AWS S3 integration for model file"
git push heroku main
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
4. **AWS S3 Storage**: The similarity.pkl model file is stored in AWS S3 and is dynamically loaded in the app using boto3.
5. **Deployment**: The app is deployed on Heroku for easy access. You can view the live app [here](https://your-app-name.herokuapp.com).

## Project Structure

- `notebooks/`: Contains Jupyter notebooks used for developing and training the model.
- `app.py`: Streamlit app for running the UI.
- `model/`: Contains the saved model and data for recommendations.
- `requirements.txt`: List of dependencies needed to run the project.

## Future Enhancements

- Implement more sophisticated recommendation algorithms such as collaborative filteringo or a hybrid approach.
- Improve UI design and add additional filters.
- Expand the dataset to include more anime titles.



