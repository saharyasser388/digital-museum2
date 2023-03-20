from django.contrib import admin
from . import models


# Register your models here.
'''
admin.site.register(models.ArtObject)
admin.site.register(models.Hall)
admin.site.register(models.Description)
admin.site.register(models.Paremenant_Collection)
admin.site.register(models.Borrowed_Collection)
admin.site.register(models.other)
admin.site.register(models.painting)
admin.site.register(models.Chariot)
admin.site.register(models.Holding)
admin.site.register(models.ArtStory)
'''


@admin.register(models.ArtStory)
class ArtStoryAdmin(admin.ModelAdmin):
    list_per_page = 7
    
       

@admin.register(models.painting)
class paintingAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['artist_name']

@admin.register(models.Holding)
class HoldingAdmin(admin.ModelAdmin):
    list_per_page = 10

    
@admin.register(models.other)
class otherAdmin(admin.ModelAdmin):
    list_per_page = 10



@admin.register(models.Chariot)
class ChariotAdmin(admin.ModelAdmin):
    list_per_page = 7
    list_display = ['object_number', 'chassis_number', 'reign']
    ordering = ['object_number']   

@admin.register(models.Borrowed_Collection)
class Borrowed_CollectionAdmin(admin.ModelAdmin):
    list_per_page = 10
  

@admin.register(models.Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['description']
    


@admin.register(models.Permenant_Collection)
class Paremenant_CollectionAdmin(admin.ModelAdmin):
    list_per_page = 7

class ArtObjectInline (admin.TabularInline):
    model = models.ArtObject

class DescriptionInline (admin.TabularInline):
    model = models.Description
 
class ArtStoryInline(admin.StackedInline):
    model = models.ArtStory

class Borrowed_CollectionAdminInline(admin.TabularInline):
    model = models.Borrowed_Collection

class PermenantCollectionAdminInline(admin.TabularInline):
    model = models.Permenant_Collection

class ChariotInline(admin.TabularInline):
    model = models.Chariot

class otherInline(admin.TabularInline):
    model = models.other

class HoldingInline(admin.TabularInline):
    model = models.Holding

class paintingInline(admin.TabularInline):
    model = models.painting



@admin.register(models.ArtObject)
class ArtObjectAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline ,ArtStoryInline,Borrowed_CollectionAdminInline, PermenantCollectionAdminInline, paintingInline, ChariotInline,otherInline,HoldingInline ]
    list_per_page = 10
    list_display = ['name', 'type', 'hall','Description']
    ordering = ['type']

@admin.register(models.Hall)
class HallAdmin(admin.ModelAdmin):
    inlines = [ArtObjectInline]
    list_per_page = 10
    list_display = ['name','hall_number']
    ordering = ['name']
