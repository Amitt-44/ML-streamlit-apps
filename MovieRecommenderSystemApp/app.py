import pickle 
import streamlit as st 
import pandas as pd
import requests 

def recommend(movie):
    # Get the index of the movie from the DataFrame
    movie_index = movies[movies['title'] == movie].index[0]
    # Get the similarity scores for the selected movie
    distances = similarity[movie_index]
    # Sort the movies based on similarity scores and get the top 5 recommendations
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

# Load the similarity matrix and movie data
similarity = pickle.load(open('MovieRecommenderSystemApp/similarity.pkl_part0', 'rb'))
movies_dict = pickle.load(open('MovieRecommenderSystemApp/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit app title
st.title('Movie Recommender System')

# Dropdown menu for selecting a movie
selected_movie_name = st.selectbox('Movie name', movies['title'].values)

# Button to get recommendations
if st.button('Recommend'):
    names = recommend(selected_movie_name)
    
    # Display recommended movies
    for name in names:
        st.text(name)
