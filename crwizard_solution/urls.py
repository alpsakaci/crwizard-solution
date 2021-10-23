from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from solution import views

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^auth/', include('social_django.urls', namespace='social')),
]
