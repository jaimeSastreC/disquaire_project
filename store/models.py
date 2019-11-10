from django.db import models

# Create your models here.
# ARTISTS = {
#   'francis-cabrel': {'name': 'Francis Cabrel'},
#   'lej': {'name': 'Elijay'},
#   'rosana': {'name': 'Rosana'},
#   'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
# }
#
#
# ALBUMS = [
#   {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
#   {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
#   {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
# ]


class Artist(models.Model):
    name = models.CharField(max_length=64, unique=True)
    #albums = models.ManyToManyField(Album, through='Artist_Album', related_name='artistes')

    def __str__(self):
        """
        nom de l'Artiste
        """
        return self.name

class Album(models.Model):
    reference = models.IntegerField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Date de parution")
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=128)
    picture = models.URLField(null=True, default="store/img/Sarbacane.jpg")
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        """
        nom de l'Album
        """
        return self.title

# class Artist_Album(models.Model):
#     id_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     id_album = models.ForeignKey(Album, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "table liaison Artiste Album"

class Contact(models.Model):
    email = models.EmailField(max_length=64)
    name = models.CharField(max_length=64)
    #albums = models.ManyToManyField(Album, through='Booking', related_name='+')

    def __str__(self):
        """
        nom du Contact
        """
        return self.name

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                verbose_name="Date de réservation")
    contacted = models.BooleanField(default=False)
    id_contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    id_album = models.OneToOneField(Album, on_delete=models.CASCADE)

    def __str__(self):
        """
        nom du Contact
        """
        return "Client: {}, disque: {}".format(self.id_contact, self.id_album)