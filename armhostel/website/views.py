from django.shortcuts import redirect, render

from website.translations import translateAboutUs, translateBook, translateContacts, translateHome, translateServices

def index(request):
    return redirect('/eng/')

def homePage(request, language):
    ctx = translateHome(language)
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