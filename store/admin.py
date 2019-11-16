from django.contrib import admin
from store.models import Artist, Album, Contact

class ArtistAdmin(admin.ModelAdmin):
   list_display   = ('name', 'albums')
   name_hierarchy = 'name'
   ordering       = ('name', )
   search_fields  = ('name',)

class AlbumAdmin(admin.ModelAdmin):
   list_display   = ('title', 'reference', 'available')
   list_filter = ('artists', )
   name_hierarchy = 'title'
   ordering       = ('title', )
   search_fields  = ('title', 'reference')

# class ArticleAdmin(admin.ModelAdmin):
#    list_display   = ('titre', 'auteur', 'date')
#    list_filter    = ('auteur','categorie',)
#    date_hierarchy = 'date'
#    ordering       = ('date', )
#    search_fields  = ('titre', 'contenu')

admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Contact)