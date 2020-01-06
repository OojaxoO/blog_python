"""blog_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import importlib

from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', get_swagger_view()),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

router = routers.DefaultRouter()
url_view_set = {}
APP = ['blog', 'user']
for i in APP:
    urls = importlib.import_module(i + '.urls')
    root = getattr(urls, 'url_root', i)
    view_sets = getattr(urls, 'url_view_set', {})
    views = getattr(urls, 'url_view', [])
    url_view_set.update({root + '/' + k: v for k, v in view_sets.items()})
    urlpatterns.append(path(root + '/', include(views)))

for k, v in url_view_set.items():
    router.register(k, v, base_name=k)

urlpatterns.append(path('', include(router.urls)))
