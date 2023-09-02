from django.http import HttpResponse
from django.shortcuts import redirect, render
from website.models import RoomPhoto, Tour, Room

from website.translations import translateAboutUs, translateBook, translateContacts, translateHome, translateRoom, translateServices

def index(request):
    return redirect('/eng/')

def homePage(request, language):
    ctx = translateHome(language)
    ctx.update({'tours': Tour.objects.all()})
    ctx.update({ 'rooms': Room.objects.all()})
    return render(request, 'website/home.html', context=ctx)

def book(request, language):
    ctx = translateBook(language)
    return render(request, 'website/book.html', context=ctx)

def aboutus(request, language):
    ctx = translateAboutUs(language)
    return render(request, 'website/aboutus.html', context=ctx)

def services(request, language):
    ctx = translateServices(language)
    return render(request, 'website/services.html', context=ctx)

def contact(request, language):
    ctx = translateContacts(language)
    return render(request, 'website/contacts.html', context=ctx)

def reception(request):
    return render(request, 'website/reception.html', context={})

def roomPhotoGallery(request, language, roomId):
    room = Room.objects.get(id=roomId)
    ctx = translateRoom(language)
    ctx.update({ 'photos': RoomPhoto.objects.filter(room=room),
                'room': room })
    return render(request, 'website/room.html', context=ctx)

def changeLanguage(request, language):
    url = request.GET['page']
    tokens = url.split('/')
    tokens = tokens[1:-1]
    tokens[0] = language
    newUrl = '/'
    for token in tokens:
        newUrl += token + '/'
    return redirect(newUrl)