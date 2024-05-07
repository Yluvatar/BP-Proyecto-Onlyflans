
from django.urls import path, include

from django.contrib import admin
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name='index'),
    path('about/', v.about, name='about'),
    path('welcome/', v.welcome, name='welcome'),
    path('contacto/', v.contacto, name='contacto'),
    path('contact_form/', v.contact_view, name='contact_form'),
    path('contacto_exitoso/', v.contact_view_exito, name='contacto_exitoso'),
    path('accounts/', include("django.contrib.auth.urls")),
]
