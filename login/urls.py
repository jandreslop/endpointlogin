from django.urls import path
from .views import NombreUsuarioView

urlpatterns =[
    path('nombreusuario/', NombreUsuarioView.as_view())

]