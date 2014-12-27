from django.contrib.sitemaps import Sitemap
from django.db.models.loading import get_model


Room = get_model('bb', 'Property')


class RoomSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Room.objects.all()

    def lastmod(self, obj):
        return obj.edit_date



sitemaps = {
    'rooms': RoomSitemap,

}