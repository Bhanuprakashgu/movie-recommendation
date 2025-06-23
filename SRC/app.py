import joblib
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a41be46f4ce2161a5fb53780683de5db"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path', '')  # Use get to avoid KeyError
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies_name = []
    recommended_poster = []
    
    for i in distances[1:7]:  # Get top 6 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        recommended_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    
    return recommended_movies_name, recommended_poster

# Streamlit app
st.header("Movies Recommendation System Using Machine Learning")

# Load models and data
movies = joblib.load(r'C:\ML\movie recommendation\SRC\models\movie_list.sav')
similarity = joblib.load(r'C:\ML\movie recommendation\SRC\models\similarity.sav')

movie_list = movies['title'].values
selected_movie = st.selectbox('Type or select a movie to get recommendations', movie_list)

if st.button('Show recommendation'):
    recommended_movies_name, recommended_poster = recommend(selected_movie)
    
    # Display recommendations
    cols = st.columns(5)
    for i, col in enumerate(cols):
        if i < len(recommended_movies_name):  # Check to avoid index errors
            with col:
                st.text(recommended_movies_name[i])
                st.image(recommended_poster[i])

