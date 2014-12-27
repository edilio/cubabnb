from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from apps.bb.sitemaps import sitemaps

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.bb.views.html.home', name='home'),
    url(r'^en/', include('apps.bb.urls.html')),
    url(r'^api/v1/', include('apps.bb.urls.api')),
    url(r'^api/v1/docs/', include('rest_framework_swagger.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Seo
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', include('robots.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)