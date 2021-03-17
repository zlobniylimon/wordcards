from django.db import models
from django.contrib.auth.models import User

class DeckCards(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

	def __str__(self):
		return str(self.name)

class Card(models.Model):
	word = models.CharField(max_length=100)
	translated_word = models.CharField(max_length=100)
	deck = models.ForeignKey(DeckCards, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.word)+'|'+str(self.deck)