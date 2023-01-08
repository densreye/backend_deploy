from rest_framework.views import APIView
from rest_framework.response import Response
from auth_manage.serializers import UploadSerializer
from django.core.files.storage import default_storage
from rest_framework import status
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import jwt
import os.path

FILES_PATH = "FILES/"
PATH_REGEX = r"[\/]+([a-z_\-\s0-9]+\/)+[a-z_\-\s0-9]+\.[a-zA-Z]+$"
JWT_KEY = 'YoSoloQuieroPegqrEnLaRadioParaGanarMiPrimerMillon'
JWT_ALGORITM = 'HS256'

media_types = {
    '.aac':	'audio/aac',
    '.abw':	'application/x-abiword',
    '.arc':	'application/x-freearc',
    '.avif':	'image/avif',
    '.avi':	'video/x-msvideo',
    '.azw':	'application/vnd.amazon.ebook',
    '.bin':	'application/octet-stream',
    '.bmp':	'image/bmp',
    '.bz':	'application/x-bzip',
    '.bz2':	'application/x-bzip2',
    '.cda':	'application/x-cdf',
    '.csh':	'application/x-csh',
    '.css':	'text/css',
    '.csv':	'text/csv',
    '.doc':	'application/msword',
    '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    '.eot': 'application/vnd.ms-fontobject',
    '.epub': 'application/epub+zip',
    '.gz': 'application/gzip',
    '.gif': 'image/gif',
    '.htm': 'text/html',
    '.html': 'text/htm',
    '.ico': 'image/vnd.microsoft.icon',
    '.ics': 'text/calendar',
    '.jar': 'application/java-archive',
    '.jpeg': 'image/jpeg',
    '.jpg': 'image/jpeg',
    '.js': 'text/javascript',
    '.json': 'application/json',
    '.jsonld': 'application/ld+json',
    '.mid': 'audio/midi ',
    '.midi': 'audio/x-midi',
    '.mjs': 'text/javascript',
    '.mp3': 'audio/mpeg',
    '.mp4': 'video/mp4',
    '.mpeg': 'video/mpeg',
    '.mpkg': 'application/vnd.apple.installer+xml',
    '.odp': 'application/vnd.oasis.opendocument.presentation',
    '.ods': 'application/vnd.oasis.opendocument.spreadsheet',
    '.odt': 'application/vnd.oasis.opendocument.text',
    '.oga': 'audio/ogg',
    '.ogv': 'video/ogg',
    '.ogx': 'application/ogg',
    '.opus': 'audio/opus',
    '.otf': 'font/otf',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.php': 'application/x-httpd-php',
    '.ppt': 'application/vnd.ms-powerpoint',
    '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    '.rar': 'application/vnd.rar',
    '.rtf': 'application/rtf',
    '.sh': 'application/x-sh',
    '.svg': 'image/svg+xml',
    '.tar': 'application/x-tar',
    '.tif': 'image/tiff',
    '.tiff': 'image/tif',
    '.ts': 'video/mp2t',
    '.ttf': 'font/ttf',
    '.txt': 'text/plain',
    '.vsd': 'application/vnd.visio',
    '.wav': 'audio/wav',
    '.weba': 'audio/webm',
    '.webm': 'video/webm',
    '.webp': 'image/webp',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
    '.xhtml': 'application/xhtml+xml',
    '.xls': 'application/vnd.ms-excel',
    '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    '.xml': 'text/xml',
    '.xul': 'application/vnd.mozilla.xul+xml',
    '.zip': 'application/zip',
    '.3gp': 'video/3gpp',
    '.3g2': 'ideo/3gpp2',
    '.7z': 'application/x-7z-compressed',
}


class UploadViewSet(APIView):
    serializer_class = UploadSerializer

    def post(self, request):
        #FIXME Seguridad: Debemos implementar seguridad en este modulo
        try:
            file_uploaded = request.FILES.get('file_uploaded')
            path = request.POST.get('path')

            if file_uploaded == None:
                return Response({'msg': "file_uploaded es un campo requerido"}, status=status.HTTP_400_BAD_REQUEST)
            if path == None:
                return Response({'msg': "path es un campo requerido"}, status=status.HTTP_400_BAD_REQUEST)

            if not esFilePath(path):
                return Response({'msg': "path no representa la ruta de un archivo"}, status=status.HTTP_400_BAD_REQUEST)

            # content_type = file_uploaded.content_type
            # nombre_archivo = file_uploaded.name
            file_path = obtener_file_path(path)
            
            # eliminamos si el archivo existe
            if default_storage.exists(file_path):
                default_storage.delete(file_path)

            # guardamos el archivo y respondemos
            file_name = default_storage.save(file_path, file_uploaded)
            data_for_encoded = obtener_hash_file(path)
            return Response({'path': path, 'jwt': data_for_encoded})
        except Exception as e:
            return Response({'msg': "ha ocurrido un problema"}, status=status.HTTP_400_BAD_REQUEST)


class GetFile(APIView):
    def get(self, request, hash):
        return reponder_archivo(hash)


def esFilePath(path):
    # FIXME Hacer que funcione la validacion del filepath
    """ 
    if re.match(PATH_REGEX, path):
		return True
	return False 
    """
    return True


def reponder_archivo(hash):
    data = decode(hash)
    if data == None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    path = data['path']
    path = obtener_file_path(path)
    try:
        if not default_storage.exists(path):
            return Response(status=status.HTTP_404_NOT_FOUND)
        file = default_storage.open(path)
        mime_type = obtener_content_type(path)
        response = HttpResponse(FileWrapper(
            file), content_type=mime_type)
        response['Content-Disposition'] = f'filename={obtener_filename(path)}'
        return response
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)


def obtener_file_path(path):
    return f'{FILES_PATH}/{path}'


# JWT ------------------------------------------------------------------------------

def obtener_content_type(path):
    # FIXME Hacer esto mas robusto
    extension = f'{os.path.splitext(path)[1]}'
    media_type = media_types[extension]
    return media_type or 'application/octet-stream'

def obtener_filename(path):
    head, tail = os.path.split(path)
    return tail

def encode_data(data):
    return jwt.encode(data, JWT_KEY, JWT_ALGORITM)

def obtener_hash_file(path):
    return encode_data({'path': path})

def decode(encode):
    try:
        return jwt.decode(encode, JWT_KEY, JWT_ALGORITM)
    except Exception as e:
        return None


def guardarArchivo(archivo,ruta):
    file_uploaded = archivo
    path = ruta

    if file_uploaded == None:
        raise Exception("file_uploaded es un campo requerido") 
        
    if path == None:
        raise Exception("path es un campo requerido") 
        

    if not esFilePath(path):
        raise Exception("path no representa la ruta de un archivo") 

    # content_type = file_uploaded.content_type
    # nombre_archivo = file_uploaded.name
    file_path = obtener_file_path(path)
    
    # eliminamos si el archivo existe
    if default_storage.exists(file_path):
        default_storage.delete(file_path)

    # guardamos el archivo y respondemos
    file_name = default_storage.save(file_path, file_uploaded)
    data_for_encoded = obtener_hash_file(path)
    return {'path': path, 'jwt': data_for_encoded}

def eliminarArchivo(path):
    file_path=obtener_file_path(path)
    if not default_storage.exists(file_path):
        raise Exception("No se encontró el archivo") 
    default_storage.delete(file_path)

def obtenerArchivosDirectorio(carpeta):
    directories, files = default_storage.listdir(FILES_PATH+carpeta)
    return directories, files