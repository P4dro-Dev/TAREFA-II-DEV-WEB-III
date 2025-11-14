from django.contrib import admin
from django.urls import path, include
# Front Controller: central routing point
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sistema.urls')),
]
