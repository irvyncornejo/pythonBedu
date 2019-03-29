"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin
from platzigram import vistas as local_views # Se renombran las vistas en ambos casos para poder trabajar as...
from posts import views as posts_views

urlpatterns = [
    url('hello/', local_views.hello_world),
    url('sorted/', local_views.sorted_integers), #sorted/?numbers=3,58,78,3 lo que ingresamos en el navegador
    url('hi/<str:name>/<int:age>/', local_views.say_hi), 
    url('posts/', posts_views.list_posts),
    # url(r'^admin/', admin.site.urls),
]
