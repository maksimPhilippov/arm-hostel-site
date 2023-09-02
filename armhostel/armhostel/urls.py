"""
URL configuration for armhostel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from website.views import aboutus, book, contact, homePage, services, index, reception, roomPhotoGallery, changeLanguage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('changelanguage/<slug:language>', changeLanguage),
    path('reception/', reception),
    path('<slug:language>/', homePage, name = 'home'),
    path('<slug:language>/tour/', homePage),
    path('<slug:language>/book/', book),
    path('<slug:language>/aboutus/', aboutus),
    path('<slug:language>/services/', services),
    path('<slug:language>/contact/', contact),
    path('<slug:language>/room/<int:roomId>', roomPhotoGallery)
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)