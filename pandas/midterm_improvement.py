import pandas as pd

movies = pd.DataFrame({
    "Title": ["Inception", "Dangal", "Avatar", "3 Idiots", "Joker", "Drishyam"],
    "Genre": ["Sci-Fi", "Drama", "Action", "Comedy", "Drama", "Thriller"],
    "Rating": [8.8, 8.3, 7.8, 8.4, 8.1, 8.2],
    "Year": [2010, 2016, 2009, 2009, 2019, 2015],
    "Duration": [148, 161, 162, 170, 122, 163],
    "Language": ["English", "Hindi", "English", "Hindi", "English", "Hindi"]
})

print(movies[movies["Year"] > 2010]["Title"])
print(movies[movies["Genre"].isin(['Comedy','Drama'])])
movies['Rating_Percent'] = movies['Rating'] * 10
print(movies.groupby(["Language"])["Title"].aggregate(["count"]))
