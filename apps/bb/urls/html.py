from ..views import html

from django.conf.urls import patterns, url

urlpatterns = patterns('bb.views',
    url(r'^rooms$', html.PropertyPageView.as_view(), name='property_list'),
    url(r'^rooms/(?P<slug>[-\w\d]+)/$', html.PropertyDetail.as_view(), name='property_detail'),
)