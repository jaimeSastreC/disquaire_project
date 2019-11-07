#_-*- coding: utf-8 -*-
from django.http import HttpResponse
from store.models import Album
from django.shortcuts import render, get_object_or_404
from datetime import datetime as dt
from store.models import Artist, Album, Contact, Booking


def index(request):
    message = "salut les terriens!"
    return  HttpResponse(message)

def listing(request):
    albums = ["<li>titre: {} - id: {}</li>".format(album.title, album.id) for album in Album.objects.all()]
    message = """
    <h1>Bienvenue chez le Disquaire</h1>
    <ul>{}</ul>
    """.format("\n".join(albums))
    return HttpResponse(message)

def detail(request, album_id):
    """ http://127.0.0.1:8000/store/1/
    """
    id =int(album_id)
    album = get_object_or_404(Album, id=id)
    dd = album.created_at
    date = "-".join(str(x) for x in [dd.day, dd.month, dd.year])
    artistes = album.artistes.all()
    message = "le nom de l'album est {0}.<br/> Il a été écrit le {1} - {2}".format(album.title, date, artistes[0])
    return HttpResponse(message)

def search(request):
    """ Requête Auteur
    http://127.0.0.1:8000/store/search/?query=Rosana
    """
    query = request.GET['query']
    if not query:
         message = "Aucun artiste n'est demandé"
    else:
        message = "artiste trouvé: {}".format(query)
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