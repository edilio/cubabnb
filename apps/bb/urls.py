__author__ = 'edilio'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = patterns('bb.views',
    url(r'^provinces/$', views.ProvinceList.as_view()),
    url(r'^provinces/(?P<pk>[0-9]+)/$', views.ProvinceDetail.as_view()),
    url(r'^municipalities/$', views.MunicipalityList.as_view()),
    url(r'^municipalities/(?P<pk>[0-9]+)/$', views.MunicipalityDetail.as_view()),
    url(r'^languages/$', views.LanguageList.as_view()),
    url(r'^languages/(?P<pk>[0-9]+)/$', views.LanguageDetail.as_view()),
    url(r'^properties/$', views.PropertyList.as_view()),
    url(r'^properties/(?P<pk>[0-9]+)/$', views.PropertyDetail.as_view()),
    url(r'^contacts/$', views.ContactList.as_view()),
    url(r'^contacts/(?P<pk>[0-9]+)/$', views.ContactDetail.as_view()),
    url(r'^guides/$', views.GuideList.as_view()),
    url(r'^guides/(?P<pk>[0-9]+)/$', views.GuideDetail.as_view()),
    url(r'^review-guides/$', views.ReviewGuideList.as_view()),
    url(r'^review-guides/(?P<pk>[0-9]+)/$', views.ReviewGuideDetail.as_view()),
    url(r'^review-properties/$', views.ReviewPropertyList.as_view()),
    url(r'^review-properties/(?P<pk>[0-9]+)/$', views.ReviewPropertyDetail.as_view()),
    url(r'^property-pictures/$', views.PropertyPictureList.as_view()),
    url(r'^property-pictures/(?P<pk>[0-9]+)/$', views.PropertyPictureDetail.as_view()),
    url(r'^facilities/$', views.FacilityList.as_view()),
    url(r'^facilities/(?P<pk>[0-9]+)/$', views.FacilityDetail.as_view()),
    url(r'^property-facilities/$', views.PropertyFacilityList.as_view()),
    url(r'^property-facilities/(?P<pk>[0-9]+)/$', views.PropertyFacilityDetail.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)