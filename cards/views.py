from django.shortcuts import render, redirect, get_object_or_404
from .models import DeckCards, Card
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
	if request.method == "POST":
		if request.POST.get('new_deck'):
			new_deck = DeckCards(user_id=request.user.id, name=request.POST['new_deck'])
			new_deck.save()
			messages.success(request, f'New deck "{new_deck.name}" has been created')
			return redirect('home')
		elif request.POST.get('delete'):
			deck = DeckCards.objects.get(id__exact=request.POST['delete'])
			deck.delete()
			messages.info(request, 'Deck has been deleted')
			return redirect('home')
	else:
		if request.user.is_authenticated:
			users_decks = DeckCards.objects.filter(user_id__exact=request.user.id)
			return render(request, 'cards/home.html', {'decks':users_decks})
		return render(request, 'cards/home.html', {'decks':None})

def deckcards(request, deckid):
	deck = get_object_or_404(DeckCards, id=deckid)
	cards = Card.objects.filter(deck__exact=deckid) 
	return render(request, 'cards/watchcards.html', {'cards':cards, 'deck':deck})

def edit(request, deckid):
	if request.method == "POST":
		if request.POST.get('new_card'):
			word = request.POST['word']
			translated_word = request.POST['translated_word'] 
			new_card = Card(deck_id = deckid, word=word, translated_word=translated_word)
			new_card.save()
			messages.success(request, 'New card has been added')
			return redirect('edit', deckid=int(deckid))
		elif request.POST.get('delete'):
			deck = Card.objects.get(id__exact=request.POST['delete'])
			deck.delete()
			messages.info(request, 'Card has been deleted')
			return redirect('edit', deckid=int(deckid))
	else:
		deck = get_object_or_404(DeckCards, id=deckid)
		cards = Card.objects.filter(deck__exact=deckid)
		if request.user.id == deck.user_id:
			return render(request, 'cards/deck_editor.html', {'deck':deck, 'cards':cards}) 
		else:
			return render(request, 'cards/deck_editor.html', {'deck':None})