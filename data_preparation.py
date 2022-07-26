import pandas as pd
import json
import pickle
import os
import warnings

import pandas as pd
from pandas.core.common import SettingWithCopyWarning

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


# https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/code?datasetId=138&sortBy=voteCount


credits = pd.read_csv('data/tmdb_5000_credits.csv')
movies = pd.read_csv('data/tmdb_5000_movies.csv')


def data_preparation(dataframe, column_list):
    for column in column_list:
        dataframe[column] = dataframe[column].apply(json.loads)
        for index, i in dataframe.iterrows():
            column_list_part = [partition['name'] for partition in i[column]]
            dataframe.loc[index, column] = str(column_list_part)

data_preparation(movies, ['genres', 'keywords', 'spoken_languages'])
data_preparation(credits, ['cast'])

# Get Director
def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']

credits['crew']=credits['crew'].apply(json.loads)
credits['crew'] = credits['crew'].apply(get_director)
credits.rename(columns={'crew':'director'},inplace=True)

movies = movies.merge(credits,left_on='id',right_on='movie_id',how='left')

df = movies[['id','original_title','overview','genres','cast','vote_average', 'director','keywords']]
df['tags'] = df['overview'] + df['genres'] + df['keywords'] + df['cast'] + df['director']

final_data = df[['id', 'original_title', 'tags']]
final_data.dropna(inplace=True)


#################################
# TF-IDF'in Problemimiz için Elde Edilmesi
#################################

tfidf = TfidfVectorizer(stop_words='english')
final_data['tags'] = final_data['tags'].fillna('')
tfidf_matrix = tfidf.fit_transform(final_data['tags'])
tfidf_matrix.shape

#################################
# 2. Cosine Similarity Matrisinin Oluşturulması
#################################

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

cosine_sim.shape

os.mkdir('model')
pickle.dump(final_data,open('model/movie_list.pkl', 'wb'))
pickle.dump(cosine_sim,open('model/similarity.pkl', 'wb'))