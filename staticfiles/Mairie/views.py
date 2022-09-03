from django.shortcuts import render, redirect
from .models import Album
from .models import Avis
from .models import Evenement
from .models import News
from .models import Une_photo
from .models import Doc
from .models import Bureau_municipal
from .models import Demarche
from .formulaires import DemarcheForm


def indexPage(request):
    albums = Album.objects.all()
    docs = Doc.objects.all()
    avis = Avis.objects.all()
    news = News.objects.all()
    events = Evenement.objects.all()
    unes = Une_photo.objects.all()
    return render(request, 'index.html', {'avis': avis,'albums': albums,'news': news, 'events': events, 'unes': unes, 'docs': docs})


def contactPage(request):
    docs = Doc.objects.all()
    events = Evenement.objects.all()
    albums = Album.objects.all()
    avis = Avis.objects.all()
    return render(request, 'phone-numbers.html', {'events': events, 'avis': avis, 'albums': albums, 'docs': docs})

def contact_maire(request):
    albums = Album.objects.all()
    avis = Avis.objects.all()
    events = Evenement.objects.all()
    docs = Doc.objects.all()
    return render(request, 'contact.html', {'events': events, 'avis': avis, 'albums': albums, 'docs': docs})

def documents(request):
    docs = Doc.objects.all()
    avis = Avis.objects.all()
    albums = Album.objects.all()
    return render(request, 'document-list.html', {'albums': albums, 'avis': avis, 'docs': docs})

def events(request):
    events = Evenement.objects.all()
    docs = Doc.objects.all()
    albums = Album.objects.all()
    return render(request, 'event-list.html', {'albums':albums, 'events': events, 'docs': docs})


def event_show(request, id):
    event = Evenement.objects.get(pk=id)
    events = Evenement.objects.all()
    albums = Album.objects.all()
    docs = Doc.objects.all()
    return render(request, 'event-detail.html', {'albums':albums, 'events': events,'event': event, 'docs': docs})

def galeries(request):
    albums = Album.objects.all()
    docs = Doc.objects.all()
    return render(request, 'gallery-list.html', {'albums' : albums, 'docs': docs})

def galerie_photos(request, id):
    album = Album.objects.get(pk=id)
    albums = Album.objects.all()
    docs = Doc.objects.all()
    return render(request, 'gallery-detail.html', {'albums': albums, 'album': album, 'docs': docs})

def conseil(request):
    docs = Doc.objects.all()
    membre_bureau = Bureau_municipal.objects.all()
    return render(request, 'town-council.html',{'docs': docs, 'membre_bureau': membre_bureau})

def post(request):
    avis = Avis.objects.all()
    docs = Doc.objects.all()
    news = News.objects.all()
    albums = Album.objects.all()
    return render(request, 'post-list.html', {'albums': albums, 'news': news, 'docs': docs, 'avis': avis})

def post_show(request, id):
    docs = Doc.objects.all()
    avis = Avis.objects.all()
    news = News.objects.get(pk=id)
    albums = Album.objects.all()
    return render(request, 'post-detail.html', {'albums': albums, 'news': news, 'docs': docs, 'avis': avis})

def avis(request):
    docs = Doc.objects.all()
    avis = Avis.objects.all()
    albums = Album.objects.all()
    return render(request, 'notice-list.html', {'albums': albums, 'avis': avis, 'docs': docs})

def avis_show(request, id):
    aviss = Avis.objects.all()
    avis = Avis.objects.get(pk=id)
    docs = Doc.objects.all()
    return render(request, 'notice-detail.html', {'avis': avis, 'aviss': aviss, 'docs': docs})

def histoire(request):
    docs = Doc.objects.all()
    avis = Avis.objects.all()
    albums = Album.objects.all()
    events = Evenement.objects.all()
    return render(request, 'town-history.html', {'events': events, 'albums': albums, 'avis': avis, 'docs': docs})

def tour(request):
    docs = Doc.objects.all()
    events = Evenement.objects.all()
    avis = Avis.objects.all()
    albums = Album.objects.all()
    return render(request, 'virtual-tour.html', {'avis': avis, 'albums': albums, 'events': events, 'docs': docs})

def stats(request):
    docs = Doc.objects.all()
    avis = Avis.objects.all()
    albums = Album.objects.all()
    events = Evenement.objects.all()
    return render(request, 'statistics.html', {'events': events, 'albums': albums, 'avis': avis, 'docs': docs})

def elements(request):
    docs = Doc.objects.all()
    return render(request, 'elements.html', {'docs': docs})

def mairie(request):
    docs = Doc.objects.all()
    albums = Album.objects.all()
    return render(request, 'town-hall.html', {'albums': albums, 'docs': docs})

def recherche(request):
    docs = Doc.objects.all()
    albums = Album.objects.all()
    return render(request, 'search-results.html', {'albums': albums,'docs': docs})


def etat_civil(request):
    model = Demarche
    form_class = DemarcheForm
    if request.method == "POST":
        if form_class.is_valid():
            form = DemarcheForm(request.POST).save()
        return redirect('/confirmation')

    else:
        form = DemarcheForm()
    return render(request, 'etat_civil.html', {'form': form, 'dataDemarche': Demarche.objects.all()})















