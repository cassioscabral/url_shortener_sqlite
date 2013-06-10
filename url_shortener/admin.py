from django.contrib import admin
from url_shortener.models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ('url_original', 'url_modificada', 'numero_clicks')
    

    def show_url_modificada(self, obj):
      return '<a href="%s">%s</a>' % (obj.url_original, obj.url_modificada)
    show_url_modificada.allow_tags = True

admin.site.register(Url, UrlAdmin)