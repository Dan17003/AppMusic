from django.db import models

class Cancion(models.Model):
    titulo = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    comentario = models.TextField()
    etiquetas = models.CharField(max_length=255)
    calificacion = models.IntegerField()
    es_favorita = models.BooleanField(default=False)
    
    # Agregar estos campos para guardar la portada y la URL de previsualización
    portada = models.URLField(blank=True, null=True)
    preview_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo
