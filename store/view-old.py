#_-*- coding: utf-8 -*-
from django.http import HttpResponse
from .models import Album
from django.shortcuts import render, get_object_or_404
from datetime import datetime as dt
from .models import Artist, Album, Contact, Booking


def index(request):
    # filtrer attribut available, ordonner du plus récent à ancien, 12 premiers
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formated_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("/n".join(formated_albums))
    return HttpResponse(message)

def listing(request):
    albums = Album.objects.filter(available=True)
    formated_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("".join(formated_albums))
    return HttpResponse(message)

def detail(request, album_id):
    """ http://127.0.0.1:8000/store/1/
    """
    album = get_object_or_404(Album, id=album_id)
    artistes = " ".join([artiste.name for artiste in album.artists.all()])
    message = "le nom de l'album est {0}.<br/> Il a été composé par {1}".format(album.title, artistes)
    return HttpResponse(message)

def search(request):
    """ Requête Auteur
    http://127.0.0.1:8000/store/search/?query=Sarbacane
    http://127.0.0.1:8000/store/search/?query=Cabrel
    """
    query = request.GET['query']
    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)

        if not albums.exists():
            #fait une requête dans la table artists et renvoie des objets de type album
            albums = Album.objects.filter(artists__name__icontains=query)
        if not albums.exists():
            message = "Misère, nous n'avons truové aucun résultat!"

        else:
            albums = ["<li>{}</li>".format(album.title) for album in albums]
            message ="""
                Nous avons trouvé les albums correspondant à votre requête:
                <ul>
                    {}
                </ul>
                """.format("</li><li>".join(albums))




    return HttpResponse(message)




################################# méthodes didactiques ##############################

#def search(request):
    # obj = str(request.GET)
    # query = request.GET['query']
    # message = "propriété GET: {0} et requête: {1}".format(obj, query)
    # return HttpResponse(message)


# def search(request):
#     query = request.GET.get('query')
#     if not query:
#         message = "Aucun artiste n'est demandé"
#     else:
#         albums = [
#             album for album in ALBUMS
#             if query in " ".join(artist['name'] for artist in album['artists'])
#         ]
#
#         if len(albums) == 0:
#             message = "Misère de misère, nous n'avons trouvé aucun résultat !"
#         else:
#             albums = ["<li>{}</li>".format(album['name']) for album in albums]
#             message = """
#                 Nous avons trouvé les albums correspondant à votre requête ! Les voici :
#                 <ul>
#                     {}
#                 </ul>
#             """.format("</li><li>".join(albums))
#
#     return HttpResponse(message)