from django.urls import path
from .views import CategoryListView, ProductListView
urlpatterns = [
    path('category/', CategoryListView.as_view(), name='CategoryListView'),
    path('product/', ProductListView.as_view(), name='ProductListView'),
]