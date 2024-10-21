import pickle 
import streamlit as st 
import pandas as pd
import requests 

def fetch_poster(movie_id):
    # Fetch poster URL from API
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    )
    data = response.json()
    # Return the URL of the movie poster
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    # Get the index of the movie from the DataFrame
    movie_index = movies[movies['title'] == movie].index[0]
    # Get the similarity scores for the selected movie
    distances = similarity[movie_index]
    # Sort the movies based on similarity scores and get the top 5 recommendations
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

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
    names, posters = recommend(selected_movie_name)
    
    # Create columns for displaying recommendations
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])  # Display image directly from the URL
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
