from django.urls import path
from . import views


app_name = 'api_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/<int:id>/', views.buy_item, name='buy_item'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
]
