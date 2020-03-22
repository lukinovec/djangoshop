from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ItemDetailView, ItemCreateView, ItemDeleteView

urlpatterns = [
    path('', views.home, name="shop-home"),
    path('item/<int:pk>/', ItemDetailView.as_view(), name="item-detail"),
    path('item/<int:pk>/delete', ItemDeleteView.as_view(), name="item-delete"),
    path('item/new/', ItemCreateView.as_view(), name="item-create"),
    path('shop/', ItemListView.as_view(), name='shop'),
]