from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.products, name='lista_productos'),
    path('<int:id>/', views.producto_detalle, name='producto_detalle')
]