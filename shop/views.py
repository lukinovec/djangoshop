from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.core.paginator import Paginator, Page
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import Item
from users.models import Profile


items = []

# Render home page with items as an object
def home(request):
    context = {
        "items": Item.objects.all(),
    }
    return render(request, "shop/home.html", context)


# Display shop items descending by their ID so newest item is displayed first
class ItemListView(ListView):
    model = Item
    template_name = "shop/shop.html"
    context_object_name = "items"
    ordering = ["-id"]
    paginate_by = 4
    queryset = Item.objects.all()


# Render item details
class ItemDetailView(DetailView):
    model = Item


# Form for item creation, check if the user is logged in
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ["itemname", "price", "about", "image"]

    def form_valid(self, form):
        form.instance.seller = self.request.user
        form.instance.original = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.seller:
            ItemListView.queryset = Item.objects.all()
            return True
        else:
            return False


# Verifies if the current logged user is the owner of the item he's trying to update, then update or display error
class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    template_name = "shop/item_update.html"
    fields = ["itemname", "price", "about", "image"]

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.seller:
            return True
        else:
            return False


# Delete item, checks if the user is logged in and if he's an owner of that item
class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    success_url = "/shop/"

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.seller:
            ItemListView.queryset = Item.objects.all()
            return True
        else:
            return False


# Transfer item ownership to the buyer
def buy(request, pk):
    item = Item.objects.filter(pk=pk).first()
    profile = Profile.objects.filter(user=item.seller).first()
    user = request.user
    if user.profile.currency >= item.price:
        user.profile.currency = user.profile.currency - item.price
        profile.currency = profile.currency + item.price
        profile.save()
        item.seller = user
        item.for_sale = False
        item.save()
        user.save()
        messages.success(
            request, "Item received, your balance: " + str(user.profile.currency)
        )
    else:
        messages.warning(request, "Insufficient funds.")
    return redirect("shop")


# Put an item up for sale
def sell(request, pk):
    Item.objects.filter(pk=pk).update(for_sale=True)
    messages.success(request, "Item put up for sale")
    return redirect("shop")


# Return item from shop
def return_from_shop(request, pk):
    Item.objects.filter(pk=pk).update(for_sale=False)
    messages.success(request, "Item returned from the store")
    return redirect("profile")


# Main page visible after logging in
@login_required
def shop(request):
    context = {
        "items": Item.objects.all(),
    }
    return render(request, "shop/shop.html", context)
