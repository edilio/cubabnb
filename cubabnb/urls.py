from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.bb.views.home', name='home'),
    url(r'^api/v1/', include('apps.bb.urls')),
    url(r'^api/v1/docs/', include('rest_framework_swagger.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    # urlpatterns += staticfiles_urlpatterns()
    # urlpatterns += patterns('',
    #     (r'^media/images/(?P<path>.*)$', 'django.views.static.serve', {
    #     'document_root': settings.MEDIA_ROOT}))

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)