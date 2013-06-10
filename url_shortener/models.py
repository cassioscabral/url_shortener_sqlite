from django.db import models
import random
import string

class Url(models.Model):
    url_original = models.URLField(max_length=255)
    url_modificada = models.URLField(max_length=20, blank=True)
    numero_clicks = models.IntegerField(default=0)
    
    def get_absolute_url(self):
        return self.url_original


    def __unicode__(self):
        return self.url_modificada

    def palavra_aleatoria(self, tamanho=6):
        palavra = ""
        for i in range(tamanho):
            palavra += random.choice(string.letters)

        return  palavra

    def modifica_url(self, padrao_inicial="soda/"):
        return padrao_inicial + self.palavra_aleatoria()

    def save(self, *args, **kwargs):
        self.url_modificada = self.modifica_url()
        super(Url, self).save(*args, **kwargs)
