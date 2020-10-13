from django.urls import path, include 
from django.conf.urls import url
from .views import *
#todo lo de aqui es tentativo por que quiza no comprendo bien el enlazamiento de las entidades
urlpatterns = [ 

    # path('notes/',views.notes,name='notes'),
    # path('notes/<str:title>',views.edit_note,name='notes'), 
    # path('notes/delete/<str:title>',views.delete_note,name='delete_note'), 


    # path('support/', views.support,name='support'),
    path('',home,name='home'),
    path('all',events_all,name='events_all'),
    path('countries',events_in_country,name='events_in_country'),
    path('countries/<int:id_country>',events_in_country,name='events_in_country_id'),
    path('event/<int:id_event>',event_info,name='event_info'),
    ]