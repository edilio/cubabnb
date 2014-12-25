from rest_framework import generics

from ..models import (Province, Municipality, Language, Property, Contact, Guide,
                     ReviewGuide, ReviewProperty, PropertyPicture, Facility, PropertyFacility)
from ..serializers import (ProvinceSerializer, MunicipalitySerializer, LanguageSerializer,
                          PropertySerializer, ContactSerializer, GuideSerializer, ReviewGuideSerializer,
                          ReviewPropertySerializer, PropertyPictureSerializer, FacilitySerializer,
                          PropertyFacilitySerializer)


class ProvinceList(generics.ListCreateAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class ProvinceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class MunicipalityList(generics.ListCreateAPIView):
    queryset = Municipality.objects.all()
    serializer_class = ProvinceSerializer


class ReviewPropertyList(generics.ListCreateAPIView):
    queryset = ReviewProperty.objects.all()
    serializer_class = ReviewPropertySerializer


class ReviewPropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewProperty.objects.all()
    serializer_class = ReviewPropertySerializer


class MunicipalityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer


class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class GuideList(generics.ListCreateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer


class GuideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer


class ReviewGuideList(generics.ListCreateAPIView):
    queryset = ReviewGuide.objects.all()
    serializer_class = ReviewGuideSerializer


class ReviewGuideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewGuide.objects.all()
    serializer_class = ReviewGuideSerializer


class PropertyPictureList(generics.ListCreateAPIView):
    queryset = PropertyPicture.objects.all()
    serializer_class = PropertyPictureSerializer


class PropertyPictureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyPicture.objects.all()
    serializer_class = PropertyPictureSerializer


class FacilityList(generics.ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class PropertyFacilityList(generics.ListCreateAPIView):
    queryset = PropertyFacility.objects.all()
    serializer_class = PropertyFacilitySerializer


class PropertyFacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyFacility.objects.all()
    serializer_class = PropertyFacilitySerializer