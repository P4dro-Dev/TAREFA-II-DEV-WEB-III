from django.contrib import admin
from django.urls import path, include
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', views.post_hello, name='post_hello'),
]