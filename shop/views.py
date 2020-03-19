from django.shortcuts import render
from .models import Item
from django.contrib.auth.decorators import login_required

items = [
{
'seller': 'Jivek',
'itemname': 'didlo',
'price': '69,90',
'date': '18. března 2020',
'about': 'Ultimate Ass Fuck Dragon Dick 3000'
},
{
'seller': 'Ondra',
'itemname': 'Aškarakabaškarak',
'price': '99999,99',
'date': '18. března 2020',
'about': 'Ultimate Watermelon Fuck Dragon Dick 3000'
}
]

def home(request):
	context = {
	'items': Item.objects.all(),
	}
	return render(request, 'shop/home.html', context, {'title': 'Home'})

@login_required
def shop(request):
	context = {
	'items': Item.objects.all(),
	}
	return render(request, 'shop/shop.html', context, {'title': 'Shop'})