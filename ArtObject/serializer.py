from rest_framework import serializers
from .models import Hall, ArtObject,ArtStory,Holding,other,painting,Description,Permenant_Collection,Borrowed_Collection,Chariot

class ArtObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArtObject
        fields = ('id','name','hall')


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hall
        fields=('name','hall_number')

class ArtStorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ArtStory
        fields=('art_object','story')

class HoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Holding
        fields=('material')

class otherSerializer(serializers.ModelSerializer):
    class Meta:
        model=other
        fields=('object_number')

class paintingSerializer(serializers.ModelSerializer):
    class Meta:
        model=painting
        fields=('artist_name')

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Description
        fields=('art_object','description')

class Permenant_CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permenant_Collection
        fields=('date_aquired')

class Borrowed_CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Borrowed_Collection
        fields=('date_borrowed','date_returned')

class ChariotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chariot
        fields=('object_number','chassis_number','country_of_orgin','reign')