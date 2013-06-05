from django.db import models

class Url(models.Model):
    url_original = models.URLField(max_length=255)
    url_modificada = models.CharField(max_length=20)
    numero_clicks = models.IntegerField(default=0)
    
    def get_absolute_url(self):
        return self.url_original


    def __unicode__(self):
        return self.url_original

    def palavra_aleatoria():
        palavra = ""
        for i in range(6):
            palavra += random.choice(string.letters)

        return  palavra

    def save(self, *args, **kwargs):
        self.url_modificada = "modificada"
        super(Url, self).save(*args, **kwargs)
