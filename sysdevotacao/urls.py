from django.urls import path,include
from .views import *

urlpatterns = [

    path('', turmaLista.as_view(),name='turmas'),
    path('<int:pk>/', turmadetelhes.as_view(),name='editar'),
    path('Create/', turmaCriar.as_view(),name='ciar'),
    path('Votar/<int:pk>/', Votacao.as_view(),name='votar'),
    path('escola/', escolaLista.as_view(),name='votar'),
]
