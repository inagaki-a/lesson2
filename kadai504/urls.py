from django.urls import path, include
from django.conf import settings
from .views import *

app_name = 'kadai504'
urlpatterns = [
    path('new/', FruitsCreate.as_view(), name='fruits_create_view'),
    path('<int:id>', FruitsDelete.as_view(), name='fruits_delete_view'),
    path('', FruitsList.as_view(), name='fruits_list_view'),
]
