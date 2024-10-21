import pickle 
import streamlit as st 
import pandas as pd
import requests 

def fetch_poster(movie_id):
    # Fetch poster URL from API
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=YOUR_API_KEY&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    
def recommend(movie):
    # Logic to recommend movies
    # ...

# Load data
similarity = pickle.load(open('similarity.pkl_part0', 'rb'))
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Movie name ', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    # Displaying recommended movies and their posters
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])  # Display image directly from URL
    # Repeat for other columns
