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


def reg_model(model):
    admin.site.register(model)


def reg_models(models):
    for m in models:
        reg_model(m)


def reg_admin(model, admin_model):
    admin.site.register(model, admin_model)

reg_models([Language, Province, Property, ReviewProperty, ReviewGuide, PropertyPicture,
            Facility, PropertyFacility])