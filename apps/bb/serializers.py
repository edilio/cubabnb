__author__ = 'edilio'

from rest_framework import serializers
from .models import (Province, Municipality, Language, Property, Contact,
                     Guide, ReviewGuide, ReviewProperty, PropertyPicture, Facility, PropertyFacility)


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'name',)


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ('id', 'name', 'province', )


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', )


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        #fields = ('id', 'name', )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide


class ReviewGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewGuide


class ReviewPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewProperty


class PropertyPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyPicture


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility


class PropertyFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyFacility