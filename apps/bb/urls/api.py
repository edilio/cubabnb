from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import api

urlpatterns = patterns('bb.views',
    url(r'^provinces/$', api.ProvinceList.as_view()),
    url(r'^provinces/(?P<pk>[0-9]+)/$', api.ProvinceDetail.as_view()),
    url(r'^municipalities/$', api.MunicipalityList.as_view()),
    url(r'^municipalities/(?P<pk>[0-9]+)/$', api.MunicipalityDetail.as_view()),
    url(r'^languages/$', api.LanguageList.as_view()),
    url(r'^languages/(?P<pk>[0-9]+)/$', api.LanguageDetail.as_view()),
    url(r'^properties/$', api.PropertyList.as_view()),
    url(r'^properties/(?P<pk>[0-9]+)/$', api.PropertyDetail.as_view()),
    url(r'^contacts/$', api.ContactList.as_view()),
    url(r'^contacts/(?P<pk>[0-9]+)/$', api.ContactDetail.as_view()),
    url(r'^guides/$', api.GuideList.as_view()),
    url(r'^guides/(?P<pk>[0-9]+)/$', api.GuideDetail.as_view()),
    url(r'^review-guides/$', api.ReviewGuideList.as_view()),
    url(r'^review-guides/(?P<pk>[0-9]+)/$', api.ReviewGuideDetail.as_view()),
    url(r'^review-properties/$', api.ReviewPropertyList.as_view()),
    url(r'^review-properties/(?P<pk>[0-9]+)/$', api.ReviewPropertyDetail.as_view()),
    url(r'^property-pictures/$', api.PropertyPictureList.as_view()),
    url(r'^property-pictures/(?P<pk>[0-9]+)/$', api.PropertyPictureDetail.as_view()),
    url(r'^facilities/$', api.FacilityList.as_view()),
    url(r'^facilities/(?P<pk>[0-9]+)/$', api.FacilityDetail.as_view()),
    url(r'^property-facilities/$', api.PropertyFacilityList.as_view()),
    url(r'^property-facilities/(?P<pk>[0-9]+)/$', api.PropertyFacilityDetail.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)