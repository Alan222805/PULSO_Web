from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('productos/', include('Productos.urls', namespace='productos')),
]