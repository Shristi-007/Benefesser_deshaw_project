from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('accounts.urls')),
    path('', include('explore.urls')),
    path('', include('UserPage.urls')),
]