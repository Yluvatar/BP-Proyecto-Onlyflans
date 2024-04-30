
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('about/', v.about, name='about'),
    path('welcome/', v.welcome, name='welcome'),
]
