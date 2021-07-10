from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kadai504/', include('kadai504.urls')),
    path('kadai/', include('kadai.urls')),
]
