# App de Música
Este proyecto es una aplicación web de música desarrollada con Django que permite a los usuarios gestionar y reproducir canciones utilizando la API de Deezer. Los usuarios pueden buscar canciones, agregarlas a favoritos, reproducir vistas previas y ver detalles como etiquetas, comentarios y calificaciones.
## Funcionalidades

Búsqueda de canciones: Integración con la API de Deezer para buscar canciones
Gestión de favoritos: Agregar, editar y eliminar canciones de la lista de favoritos
Reproducción de música: Reproducir vistas previas de canciones directamente desde Deezer
Detalles de canciones: Ver información como título, artista, portada del álbum y más

## Estructura del proyecto

app_musica/
│
├── manage.py                      # Script principal para ejecutar comandos de Django
├── app_musica/                    # Configuración y archivos de Django
│   ├── init.py
│   ├── settings.py                # Configuración del proyecto Django
│   ├── urls.py                    # URLs del proyecto
│   ├── wsgi.py
│   └── asgi.py
│
├── canciones/                     # Aplicación Django para gestionar canciones
│   ├── migrations/                # Migraciones de la base de datos
│   ├── init.py
│   ├── admin.py                   # Configuración del panel de administración
│   ├── apps.py
│   ├── models.py                  # Modelos de datos (como Cancion)
│   ├── views.py                   # Lógica de la aplicación
│   ├── forms.py                   # Formularios para agregar canciones
│   └── templates/                 # Plantillas HTML
│       ├── buscar_cancion.html
│       ├── lista_canciones.html
│       ├── agregar_cancion.html
│       └── editar_cancion.html
│
└── requirements.txt               # Lista de dependencias del proyecto

## Requisitos

Para ejecutar este proyecto necesitas:
- **Git** (para clonar el repositorio)
- **Python 3.x**
- **pip** (administrador de paquetes para Python)
- **pip install django**
- **pip install requests** : Para realizar peticiones HTTP a la API de Deezer.
