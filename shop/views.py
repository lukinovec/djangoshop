from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
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


class ItemCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Item
	fields = ['itemname', 'price', 'about', 'image']

	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Item
	success_url = '/shop/'

	def test_func(self):
		item = self.get_object()
		if self.request.user == item.seller:
			return True
		else:
			return False

@login_required
def shop(request):
	context = {
	'items': Item.objects.all(),
	}
	return render(request, 'shop/shop.html', context, {'title': 'Shop'})