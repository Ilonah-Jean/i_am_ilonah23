from django.urls import path # type: ignore
from .views import plant_list, plant_create, plant_update, plant_delete, plant_trade

urlpatterns = [
    path('', plant_list, name='plant_list'),
    path('create/', plant_create, name='plant_create'),
    path('update/<int:pk>/', plant_update, name='plant_update'),
    path('delete/<int:pk>/', plant_delete, name='plant_delete'),
    path('trade/<int:pk>/', plant_trade, name='plant_trade'),  # New Trade URL
]