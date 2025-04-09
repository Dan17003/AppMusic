import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cancion
from .forms import CancionForm

def buscar_cancion(request):
    resultados = []
    if 'q' in request.GET:
        query = request.GET['q']
        url = f"https://api.deezer.com/search?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            resultados = data['data']
    return render(request, 'buscar_cancion.html', {'resultados': resultados})

def agregar_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_canciones')
    else:
        titulo = request.GET.get('titulo', '')
        artista = request.GET.get('artista', '')
        form = CancionForm(initial={'titulo': titulo, 'artista': artista})
    return render(request, 'agregar_cancion.html', {'form': form})

def lista_canciones(request):
    canciones = Cancion.objects.all()

    # Obtener información de Deezer para cada canción
    for cancion in canciones:
        # Hacer una solicitud a Deezer para obtener la información de la canción
        url = f"https://api.deezer.com/search?q={cancion.titulo} {cancion.artista}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data['data']:
                # Tomar la primera coincidencia (puedes elegir otra lógica si lo prefieres)
                cancion_data = data['data'][0]
                cancion.portada = cancion_data['album']['cover_medium']
                cancion.preview_url = cancion_data['preview']  # URL de previsualización de la canción
            else:
                cancion.portada = None
                cancion.preview_url = None
        else:
            cancion.portada = None
            cancion.preview_url = None

    return render(request, 'lista_canciones.html', {'canciones': canciones})

def editar_cancion(request, cancion_id):
    cancion = get_object_or_404(Cancion, id=cancion_id)
    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            form.save()
            return redirect('lista_canciones')
    else:
        form = CancionForm(instance=cancion)
    return render(request, 'editar_cancion.html', {'form': form})

def eliminar_cancion(request, cancion_id):
    cancion = get_object_or_404(Cancion, id=cancion_id)
    cancion.delete()
    return redirect('lista_canciones')
