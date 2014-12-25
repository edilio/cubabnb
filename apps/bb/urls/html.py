from ..views import html

from django.conf.urls import patterns, url

urlpatterns = patterns('bb.views',
    url(r'^properties$', html.PropertyPageView.as_view(), name='property_list'),
    url(r'^properties/(?P<slug>[-\w\d]+)/$', html.PropertyDetail.as_view(), name='property_detail'),
)