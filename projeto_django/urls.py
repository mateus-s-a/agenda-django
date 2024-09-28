"""
URL configuration for projeto_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from agenda.views import listar_evento
from agenda.urls import urlpatterns as agenda_urls

urlpatterns = [
    path('admin/', admin.site.urls), # --- rota para o admin, que serve para administrar o site [admin:login, admin:index]
    path("", include(agenda_urls)),
]


# Comandos no CMD para Django:
# python manage.py runserver --- executa o servidor
# python manage.py makemigrations --- cria as migrations; (migrations) são arquivos .py
# python manage.py migrate --- executa as migrations
# python manage.py shell --- executa o shell; (shell) é o shell do django ORM
# python manage.py dbshell --- executa o dbshell; (dbshell) é o shell do django DB SQLite
# python manage.py createsuperuser --- cria superuser, que é um usuário admin do django