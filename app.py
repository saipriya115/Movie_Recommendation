import streamlit as st#i am using streamlit library here
import pickle
import requests
import pandas as pd
#now this below function will hit on the api,now to hit on the api a library is required called
#requests
#def fetch_poster(movie_id):
    #url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format( movie_id)
   #instead of this movieid i will put .format(jo movie id mil raha hain)

    #data = requests.get(url)
    #so from that i will get response and i will convert that response into json
    #data = data.json()

   # poster_path = data['poster_path']
    #now i want to return the datas poster path,but the above is not complete path so i will
    #use the below
    #full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    #return full_path
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommended_movies=[]
    #recommended_movie_posters = []
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        #recommended_movies.append(movies.iloc[i[0]].movie_id)
        #fetch poster from API
        #recommended_movie_posters.append(fetch_poster(movie_id))
        #along with appending movies so from the above i will get poster from fetch poster
        #function and that poster i will keep appending to recommended movie posters
        recommended_movies.append(movies.iloc[i[0]].title)
        #so here everytime from movielist we are adding movie titile to the list also
        #poster we are adding to the list above
       #and while returning both of them i am returining posters and movies
    return recommended_movies#recommended_movie_posters
#in the above function simply if you give one movie in return it will give you 5 movies
movies_dict=pickle.load(open('movie_dict.pkl','rb'))#now here we will have new dataframe
#new_df in the movies_list if we want but we want array of movies names so
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')#here we have a function called title
#after that i have to add a textbox where user will type
selected_movie= st.selectbox(
    "How would you like to be contacted?",movies['title'].values)
if st.button('Show Recommendation'):
    recommended_movie_names= recommend(selected_movie)
    for i in recommended_movie_names:
        st.write(i)

#for deployment you have to create proct file
#basically you are running the file on heroku server
#setup.sh usually contains all the directories
#a last file we generate for heroku deplument a list of libraries required for this project
#to run on server
