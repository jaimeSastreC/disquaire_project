#_-*- coding: utf-8 -*-
from django.http import HttpResponse
#from .models import ALBUMS


def index(request):
    message = "salut les terriens!"
    return  HttpResponse(message)

def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """
    <ul>{}</ul>
    """.format("\n".join(albums))
    return HttpResponse(message)

def detail(requete, album_id):
    id =int(album_id)
    album = ALBUMS[id]
    artists = " ".join([artist['name'] for artist in album['artists']])
    message = "le nom de l'album est {0}. Il a été écrit par {1}".format(album['name'], artists)
    return HttpResponse(message)

#def search(request):
    # obj = str(request.GET)
    # query = request.GET['query']
    # message = "propriété GET: {0} et requête: {1}".format(obj, query)
    # return HttpResponse(message)


def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun artiste n'est demandé"
    else:
        albums = [
            album for album in ALBUMS
            if query in " ".join(artist['name'] for artist in album['artists'])
        ]

        if len(albums) == 0:
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = ["<li>{}</li>".format(album['name']) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(albums))

    return HttpResponse(message)