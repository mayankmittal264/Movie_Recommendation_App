from django.shortcuts import render
from myapp.models import Movie
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Create your views here.
def combine_features(row):
    try:
        genre_list = row['genre'].split('|')
        keyword_list = row['keywords'].split('|')
        genre_list = [genre.strip().lower() for genre in genre_list]
        keyword_list = [keyword.strip().lower() for keyword in keyword_list]
        return " ".join(genre_list)+" "+" ".join(keyword_list)
    except:
        return None


def webpage(request, *args):
    df = pd.DataFrame(list(Movie.objects.all().values()))
    df['combine_feature'] = df.apply(combine_features, axis=1)
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['combine_feature'])
    cosine_sin = cosine_similarity(count_matrix)
    recommendation = []
    if request.method == "POST":
        movie_liked = request.POST.get('Movie', '')
        try:
            movie_index = df[df.Movie_title == movie_liked]["id"].values[0]
            similar_movies = list(enumerate(cosine_sin[movie_index - 1]))
            similar_movies.sort(key=lambda x: x[1], reverse=True)
            for i in range(0, min(10, len(similar_movies))):
                movie_image = df[df.id == similar_movies[i][0] + 1]["image"].values[0]
                movie_name = df[df.id == similar_movies[i][0] + 1]["Movie_title"].values[0]
                if movie_name != movie_liked:
                    recommendation.append(Movie.objects.get(Movie_title=movie_name))
            recommend_data = {
                'Movie_List': recommendation,
            }
            return render(request, "webpage.html", recommend_data)
        except:
            return render(request, "webpage.html")
    return render(request, "webpage.html")
