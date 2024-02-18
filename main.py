import pandas as pd
import matplotlib.pyplot as plt


netflix_df = pd.read_csv('netflix_data.csv')
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]
netflix_movies = netflix_subset[["title", "country","genre", "release_year", "duration"]]
short_movies = netflix_movies[netflix_movies["duration"] < 60]
colors= []
for lab,row in netflix_movies.iterrows() :
    if row["genre"] == "Children" :
        colors.append("red")
    elif row["genre"] == "Documentaries" :
        colors.append("black")
    elif row["genre"] == "Stand-Up" :
        colors.append("yellow")
    else :
        colors.append("purple")
fig = plt.figure(figsize=(12,8))
x= netflix_movies["release_year"]
y= netflix_movies["duration"]

plt.scatter(x,y,c= colors)
plt.ylabel("Duration (min)")
plt.xlabel("Release year")
plt.title("Movie Duration by Year of Release")
plt.show()