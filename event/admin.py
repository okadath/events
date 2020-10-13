from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Country) 


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["link_1"].label = "Link 1 (https://www.google.com):"
        return form