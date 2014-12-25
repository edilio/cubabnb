__author__ = 'edilio'

from django.contrib import admin
from .models import *


@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'province')
    search_fields = ('name',)
    list_filter = ('province', )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'cell', 'email')
    search_fields = ('name', 'phone', 'cell')


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'cell', 'email')
    search_fields = ('name', 'phone', 'cell')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'bedrooms', 'bath_rooms', 'rate_per_room', 'slug')
    search_fields = ('name', 'description', 'near_by_places')
    list_filter = ('active', 'bedrooms', 'bath_rooms')


def reg_model(model):
    admin.site.register(model)


def reg_models(models):
    for m in models:
        reg_model(m)


def reg_admin(model, admin_model):
    admin.site.register(model, admin_model)

reg_models([Language, Province, ReviewProperty, ReviewGuide, PropertyPicture,
            Facility, PropertyFacility])