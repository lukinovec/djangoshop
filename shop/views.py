from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import Item


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


class ItemListView(ListView):
	model = Item
	template_name = 'shop/shop.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'items'
	ordering = ['-id']


class ItemDetailView(DetailView):
	model = Item


class ItemCreateView(LoginRequiredMixin, CreateView):
	model = Item
	fields = ['itemname', 'price', 'about', 'image']

	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()
		if self.request.user == item.seller:
			return True
		else:
			return False


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Item
	template_name = 'shop/item_update.html'
	fields = ['itemname', 'price', 'about', 'image']

	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()
		if self.request.user == item.seller:
			return True
		else:
			return False


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Item
	success_url = '/shop/'

	def test_func(self):
		item = self.get_object()
		if self.request.user == item.seller:
			return True
		else:
			return False

# Transfer item ownership to the buyer
class BuyView(LoginRequiredMixin, UpdateView):
	model = Item
	success_message = "Item bought!"

	def buy(self, request, *args, **kwargs):
		self.object = self.get_object()
		user = self.request.user
		if user.profile.currency >= self.object.price:
			user.profile.currency -= self.object.price
			self.object.seller = user.username
			self.object.for_sale = False
		else:
			messages.error(request, 'Insufficient funds.')


# Put an item up for sale
#class SellView():
#	model = Item
#	success_message = "Item put up for sale!"
def sell(request, pk):
	Item.objects.filter(pk=pk).update(for_sale=True)
	messages.success(request, 'Item put up for sale')
	return redirect('shop')

# Return item from shop
def return_from_shop(request, pk):
	Item.objects.filter(pk=pk).update(for_sale=False)
	messages.success(request, 'Item returned from the store')
	return redirect('profile')


@login_required
def shop(request):
	context = {
	'items': Item.objects.all(),
	}
	return render(request, 'shop/shop.html', context, {'title': 'Shop'})