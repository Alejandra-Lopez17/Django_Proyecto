from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('agregar/', views.agregar),
  path('borrar/<id>', views.borrar),
  path('editar/<id>', views.editar),
  path('actualizar/<id>', views.actualizar)
]