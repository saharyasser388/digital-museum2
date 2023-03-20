from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('objects', views.getArtObject),
    path('objects/<int:id>', views.getArt_id),
    path('story', views.getArtStory),
    path('chariot', views.getChariot),
    path('painting', views.getpainting),
    path('holding', views.getHolding),
    path('other', views.getother),
    path('description', views.getDescription),
    path('permenant_collection', views.getPermenant_Collection),
    path('borrowed_collection', views.getBorrowed_Collection),
    path('hall', views.getHall),
]
