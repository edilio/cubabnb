__author__ = 'edilio'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = patterns('bb.views',
    url(r'^api/v1/provinces/$', views.ProvinceList.as_view()),
    url(r'^api/v1/provinces/(?P<pk>[0-9]+)/$', views.ProvinceDetail.as_view()),
    url(r'^api/v1/municipalities/$', views.MunicipalityList.as_view()),
    url(r'^api/v1/municipalities/(?P<pk>[0-9]+)/$', views.MunicipalityDetail.as_view()),
    url(r'^api/v1/languages/$', views.LanguageList.as_view()),
    url(r'^api/v1/languages/(?P<pk>[0-9]+)/$', views.LanguageDetail.as_view()),
    url(r'^api/v1/properties/$', views.PropertyList.as_view()),
    url(r'^api/v1/properties/(?P<pk>[0-9]+)/$', views.PropertyDetail.as_view()),
    url(r'^api/v1/contacts/$', views.ContactList.as_view()),
    url(r'^api/v1/contacts/(?P<pk>[0-9]+)/$', views.ContactDetail.as_view()),
    url(r'^api/v1/guides/$', views.GuideList.as_view()),
    url(r'^api/v1/guides/(?P<pk>[0-9]+)/$', views.GuideDetail.as_view()),
    url(r'^api/v1/review-guides/$', views.ReviewGuideList.as_view()),
    url(r'^api/v1/review-guides/(?P<pk>[0-9]+)/$', views.ReviewGuideDetail.as_view()),
    url(r'^api/v1/review-properties/$', views.ReviewPropertyList.as_view()),
    url(r'^api/v1/review-properties/(?P<pk>[0-9]+)/$', views.ReviewPropertyDetail.as_view()),
    url(r'^api/v1/property-pictures/$', views.PropertyPictureList.as_view()),
    url(r'^api/v1/property-pictures/(?P<pk>[0-9]+)/$', views.PropertyPictureDetail.as_view()),
    url(r'^api/v1/facilities/$', views.FacilityList.as_view()),
    url(r'^api/v1/facilities/(?P<pk>[0-9]+)/$', views.FacilityDetail.as_view()),
    url(r'^api/v1/property-facilities/$', views.PropertyFacilityList.as_view()),
    url(r'^api/v1/property-facilities/(?P<pk>[0-9]+)/$', views.PropertyFacilityDetail.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)