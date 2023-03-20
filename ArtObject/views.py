from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ArtObjectSerializer, ArtStorySerializer,ChariotSerializer,paintingSerializer,HoldingSerializer,otherSerializer,DescriptionSerializer,Permenant_CollectionSerializer,Borrowed_CollectionSerializer,HallSerializer
from .models import ArtObject, ArtStory, Chariot,painting,Holding,other,Description,Permenant_Collection,Borrowed_Collection,Hall
# Create your views here.

@api_view()
def getArtObject(request):
        art_object = ArtObject.objects.all()
        serializer = ArtObjectSerializer(art_object, many=True)
        return Response(serializer.data)

@api_view()
def getArt_id(request,id):
        art_object = ArtObject.objects.get(pk=id)
        serializer = ArtObjectSerializer(art_object)
        return Response(serializer.data)

@api_view()
def getArtStory(request):
    art_object = ArtStory.objects.all()
    serializer = ArtStorySerializer(art_object, many=True)
    return Response(serializer.data)

@api_view()
def getChariot(request):
    art_object = Chariot.objects.all()
    serializer = ChariotSerializer(art_object, many=True)
    return Response(serializer.data)

@api_view()
def getpainting(request):
    art_object = painting.objects.all()
    serializer = paintingSerializer(art_object, many=True)
    return Response(serializer.data)

@api_view()
def getHolding(request):
    art_object = Holding.objects.all()
    serializer = HoldingSerializer(art_object, many=True)
    return Response(serializer.data)

@api_view()
def getother(request):
    art_object = other.objects.all()
    serializer = otherSerializer(art_object, many=True)
    return Response(serializer.data)

@api_view()
def getDescription(request):
    art_object = Description.objects.all()
    serializer = DescriptionSerializer(art_object, many=True)
    return Response(serializer.data)

@api_view()
def getPermenant_Collection(request):
    art_object = Permenant_Collection.objects.all()
    serializer = Permenant_CollectionSerializer(art_object, many=True)
    return Response(serializer.data)

@api_view()
def getBorrowed_Collection(request):
    art_object = Borrowed_Collection.objects.all()
    serializer = Borrowed_CollectionSerializer(art_object, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getHall(request):
    art_object = Hall.objects.all()
    serializer = HallSerializer(art_object, many=True)
    return Response(serializer.data)

