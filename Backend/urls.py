from django.contrib import admin
from django.urls import path, include
from django.urls import include, re_path
from django.views.generic.base import TemplateView

from auth_manage.files import UploadViewSet, GetFile
urlpatterns = [ 
    
    path('crm/', include('crm.urls')),
    path('web/', include('web.urls')),
    path('movil/', include('movil.urls')),
    path('front/', include('front.urls')),

    path('file/', UploadViewSet.as_view()),
    path('file/<str:hash>/', GetFile.as_view()),
    #Modo Adminstrador
    path('admin/', admin.site.urls),
    re_path(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
]
