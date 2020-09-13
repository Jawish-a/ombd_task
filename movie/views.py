from django.shortcuts import render
import requests

def movie_list(request):
    movie_title = "bat"
        # movie_title = request.GET.get("movie_title")
    url = "http://www.omdbapi.com/?apikey=7d9812cd&s="
    path = url + movie_title
    response = requests.get(path).json()

    context = {
        "response": response,
    }

    return render(request, 'movie_list.html', context)


def movie_detail(request, imdb_id):
        # movie_title = request.GET.get("movie_title")
    url = "http://www.omdbapi.com/?apikey=7d9812cd&i="
    path = url + imdb_id
    response = requests.get(path).json()

    context = {
        "movie": response,
    }

    return render(request, 'movie_detail.html', context)
