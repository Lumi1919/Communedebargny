from django.urls import path
from . import views
from django.urls import re_path
app_name = 'Mairie'
urlpatterns = [

    path('etat_civil/', views.etat_civil, name='etat_civil'),
    path('contact/', views.contactPage, name='contact'),
    path('mairie/', views.mairie, name='mairie'),
    path('contact_maire/', views.contact_maire, name='contact_maire'),
    path('documents/', views.documents, name='documents'),
    path('events/', views.events, name='events'),
    re_path('events/(?P<id>[0-9]+)$', views.event_show, name='event_show'),
    path('galeries/', views.galeries, name='galeries'),
    re_path('galerie/(?P<id>[0-9]+)$', views.galerie_photos, name='galerie_photos'),
    path('conseil/', views.conseil, name='conseil'),
    path('post/', views.post, name='post'),
    re_path('post/(?P<id>[0-9]+)$', views.post_show, name='post_show'),
    re_path('avis/(?P<id>[0-9]+)$', views.avis_show, name='avis_show'),
    path('avis/', views.avis, name='avis'),
    path('histoire/', views.histoire, name='histoire'),
    path('tour/', views.tour, name='tour'),
    path('stats/', views.stats, name='stats'),
    path('elements/', views.elements, name='elements'),
    path('', views.indexPage, name='accueil'),
    path('result/', views.recherche, name='recherche'),
]
