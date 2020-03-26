from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemDeleteView, ItemUpdateView, sell, return_from_shop
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="shop-home"),
    path('item/<int:pk>/', ItemDetailView.as_view(), name="item-detail"),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name="item-delete"),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name="item-update"),
    path('item/<int:pk>/sell/', views.sell, name="item-sell"),
    path('item/<int:pk>/return/', views.return_from_shop, name="item-return"),
    path('item/new/', ItemCreateView.as_view(), name="item-create"),
    path('shop/', ItemListView.as_view(), name='shop'),
]