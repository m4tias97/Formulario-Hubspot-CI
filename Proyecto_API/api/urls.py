
from django.urls import path
from . import views

urlpatterns = [
    path('',views.form,name='form'),
    path('TerminosYCondiciones', views.TerminosYCondiciones, name='terminos'),
    path('eliminar', views.eliminar, name='eliminar'),

]
