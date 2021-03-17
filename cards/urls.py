from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('<int:deckid>/', views.deckcards, name='watchcards'),
	path('edit/<int:deckid>/', views.edit, name='edit')
]
