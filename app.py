import pickle
import streamlit as st
import requests
import os
from PIL import Image
from dotenv import load_dotenv
import pandas as pd
logo = Image.open('images/logo.png')
frame = Image.open('images/frame.png')

load_dotenv()
API = os.getenv('MOVIE_API')

st.set_page_config(
   page_title="Film Tavsiye Sistemi",
   page_icon="🤖",
   layout="wide",
   initial_sidebar_state="expanded",
)


def get_movie_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API}&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def content_based_recommender(title, cosine_sim, dataframe):
    # index'leri olusturma
    indices = pd.Series(dataframe.index, index=dataframe['original_title'])
    indices = indices[~indices.index.duplicated(keep='last')]
    # title'ın index'ini yakalama
    movie_index = indices[title]
    # title'a gore benzerlik skorlarını hesapalama
    similarity_scores = pd.DataFrame(cosine_sim[movie_index], columns=["score"])
    # kendisi haric ilk 10 filmi getirme
    movie_indices = similarity_scores.sort_values("score", ascending=False)[1:6].index

    movie_names = []
    movie_posters = []

    for i in movie_indices[0:6]:
        # fetch the movie poster
        movie_id = dataframe.iloc[i].id
        movie_posters.append(get_movie_poster(movie_id))
        movie_names.append(movies.iloc[i]['original_title'])

    return movie_names, movie_posters


col1, col2, col3 = st.columns(3)
with col1:
    st.image(frame, width=125)

with col2:
    st.image(logo, caption='🧠 Skills of tomorrow!', width=350)

with col3:
    st.markdown("[![Foo](https://img.icons8.com/material-outlined/96/000000/github.png)](https://github.com/oguzerdo/Movie-Recommendation-System)")

st.header('Film Tavsiye Sistemi')

movies = pickle.load(open('model/movie_list.pkl', 'rb'))
cosine_sim = pickle.load(open('model/cosine_sim.pkl', 'rb'))

movie_list = movies['original_title'].values  # Tüm film isimlerini alma

selected_movie = st.selectbox("Açılır menüden film seçiniz.", movie_list) # Açılır menüde film isimlerini gösterme.

if st.button('Tavsiyeleri gör'):
    movie_names, movie_posters = content_based_recommender(selected_movie, cosine_sim, movies)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movie_posters[0])
    with col2:
        st.text(movie_names[1])
        st.image(movie_posters[1])

    with col3:
        st.text(movie_names[2])
        st.image(movie_posters[2])
    with col4:
        st.text(movie_names[3])
        st.image(movie_posters[3])
    with col5:
        st.text(movie_names[4])
        st.image(movie_posters[4])


if st.button('Şansımı denemek istiyorum'):
    random_movie = movies['original_title'].sample(1).values[0]
    st.subheader(random_movie)
    movie_names, movie_posters = content_based_recommender(random_movie, cosine_sim, movies)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movie_posters[0])
    with col2:
        st.text(movie_names[1])
        st.image(movie_posters[1])

    with col3:
        st.text(movie_names[2])
        st.image(movie_posters[2])
    with col4:
        st.text(movie_names[3])
        st.image(movie_posters[3])
    with col5:
        st.text(movie_names[4])
        st.image(movie_posters[4])
