# Integracion al resto del sistema
Crear un entorno virual

Asumiendo que sus proyectos se llaman **Backend**

Cargar Paquetes en el entorno virtual
```bash
pip install -r requirements.txt
```

Ejecutar en el entorno virtual **Backend/venv/**
```bash:
django-admin startproject Backend ../

```
Ejecutar en el entorno virtual **Backend/**
```bash:
python manage.py startapp crm

```

Añadir la ruta en el archivo **Backend/urls.py**
```python:
urlpatterns = [ 
    # las rutas que uds vayana a agregar
    path('crm/', include('crm.urls'))
]
```

Añadir la app al archivo **Backend/settings.py**

```python:
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Las APPs que necesiten#
    'crm', # Archivo necesario para CRM
]
```

## Otros
fue generado un requirements.txt

# Modelos de la Base
generar modelos a partir de una base  instalada en su maquina local

Ejecutar en el entorno virtual **Backend/**

```bash:
python manage.py inspectdb >models.py

```
