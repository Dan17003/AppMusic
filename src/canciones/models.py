from django.db import models

class Cancion(models.Model):
    titulo = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    preview_url = models.URLField(blank=True, null=True)
    imagen_url = models.URLField(blank=True, null=True)

    comentario = models.TextField(blank=True, null=True)
    etiquetas = models.CharField(max_length=255, blank=True)
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)
    es_favorita = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"
