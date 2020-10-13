from django.shortcuts import render
from .models import *
from django.utils import timezone
from django.conf import settings
# Create your views here.
def home(request):
	context = {}
	time=timezone.now()
	context["time"] = time
	# la siguiente linea, obtiene todos, los filtra si la fecha es mas grande que la fecha actual, los ordena, y devuelve
	# los que se requieran en el home, esta variable se edita en el settings
	n_events = Event.objects.all().filter(start_date__gte=timezone.now()).order_by('start_date')[:settings.N_ELEMENTS]
	context["events"] = n_events
	# .order_by('-start_date')
	# print(n_events)
	return render(request, 'home.html', context)

def events_in_country(request,id_country=""): 
	context = {}
	if id_country == "":
		all_countries = Country.objects.all()
		context["countries"] = all_countries
		return render(request, 'per_country.html', context)
	else:
		try:
			country_events = Event.objects.all().filter(country=id_country).filter(start_date__gte=timezone.now()).order_by('start_date')
			context["events"] = country_events
			context["country"]= Country.objects.get(id=id_country)
		except Exception as e:
			context["error_messages"] = "There is no such country"
	return render(request, 'per_country.html', context)

def events_all(request):
	context = {}
	all_events = Event.objects.all().filter(start_date__gte=timezone.now()).order_by('start_date')
	context["events"] = all_events
	return render(request, 'all.html', context)


def event_info(request,id_event):
	context = {}
	try:
		event = Event.objects.get(id=id_event)
		context["event"] = event
	except Exception as e:
		context["error_messages"] = "There is no such event"
	return render(request, 'event.html', context)