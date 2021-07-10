from django.urls import path, include
from django.conf import settings
from .views import *
from .service import *

app_name = 'kadai'
urlpatterns = [
    path('list/', FruitsView.as_view(), name='fruits_view'),
    path('', FruitsView.as_view(), name='fruits_view'),
    path('hello/', HelloView.as_view(), name='hello_view'),
    path('upload/', FruitsService.upload, name='upload'),
]
