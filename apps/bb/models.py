from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils import timezone


class Province(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province)

    class Meta:
        verbose_name_plural = "Municipalities"

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    cell = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=50)
    contact = models.ForeignKey(Contact)
    bedrooms = models.PositiveSmallIntegerField(default=1)
    bath_rooms = models.PositiveSmallIntegerField(default=1)
    description = models.TextField()
    rate_per_room = models.DecimalField(decimal_places=2, max_digits=6)
    near_by_places = models.TextField(default='', blank=True)

    active = models.BooleanField(default=True)

    slug = models.SlugField(max_length=250, default='', editable=False)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Properties"

    @property
    def div_amenities_names(self):
        names = []
        for amenity in self.amenities.all():
            names.append(amenity.facility.div_name)
        return names

    @property
    def pictures(self):
        return [p.picture for p in self.propertypicture_set.all()]

    @property
    def pictures_urls(self):
        return [(p.picture_url(), p.tag) for p in self.propertypicture_set.all()]

    @models.permalink
    def get_absolute_url(self):
        return ('property_detail', (), {
            'slug': self.slug,
        })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) + '-' + str(self.id)
        self.edit_date = timezone.now()
        super(Property, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Guide(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    cell = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return self.name

STAR_CHOICES = (
    (0, '0 - Stars'),
    (1, '1 - Stars'),
    (2, '2 - Stars'),
    (3, '3 - Stars'),
    (4, '4 - Stars'),
    (5, '5 - Stars'),
)


class ReviewGuide(models.Model):
    guide = models.ForeignKey(Guide)
    stars = models.PositiveSmallIntegerField(choices=STAR_CHOICES)
    note = models.TextField()
    nick_name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Review Guides"
        verbose_name = "Review Guide"


class ReviewProperty(models.Model):
    property = models.ForeignKey(Property)
    stars = models.PositiveSmallIntegerField(choices=STAR_CHOICES)
    note = models.TextField()
    nick_name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Review Properties"
        verbose_name = "Review Property"


class PropertyPicture(models.Model):
    property = models.ForeignKey(Property)
    picture = models.ImageField(upload_to=settings.UPLOAD_IMAGES_FOLDER)
    tag = models.CharField(null=True, blank=True, max_length=30)
    index = models.PositiveSmallIntegerField(default=0)

    def picture_url(self):
        url = self.picture.url
        i = url.find('/media')
        return url[i:]

    class Meta:
        ordering = ['index']

    def __unicode__(self):
        return self.property.name


class Facility(models.Model):
    name = models.CharField(max_length=50)
    div_name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Facilities"

    def __unicode__(self):
        return self.name


class PropertyFacility(models.Model):
    property = models.ForeignKey(Property, related_name='amenities')
    facility = models.ForeignKey(Facility)

    class Meta:
        verbose_name_plural = "Property Facilities"
        verbose_name = "Property Facility"

    def __unicode__(self):
        return self.property.name + " ==> " + self.facility.name