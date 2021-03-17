from django.contrib import admin

from .models import Card, DeckCards

admin.site.register(Card)
admin.site.register(DeckCards)