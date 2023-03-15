from django.db import models
from django_countries.fields import CountryField
#from django_countries.fields import CountryField

class Hall(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    halls_number = models.PositiveSmallIntegerField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
    
class ArtObject(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    TYPE_CHOICES =[
        ('CH','Chariot'),
        ('PN','Painting'),
        ('ST','Status'),
        ('HO','Holding'),
        ('OR','Other'), 
    ]
    type = models.CharField(max_length=2, choices = TYPE_CHOICES,null=True, blank=True)
    date_added = models.DateField(auto_now_add = 1)
    date_modified = models.DateField(auto_now = 1)
    hall = models.ForeignKey(Hall, related_name='Art_Object', on_delete= models.SET_DEFAULT, default='8')

    def __str__(self) -> str:
        return self.name

class Description(models.Model):
    description = models.TextField(null=True,blank=True)
    art_object = models.OneToOneField(ArtObject, related_name='Description', on_delete= models.CASCADE, primary_key= True)

    def __str__(self) -> str:
        return self.art_object.name

class ArtStory(models.Model):
    story = models.TextField(null=True,blank=True)
    art_object = models.OneToOneField(ArtObject, related_name='Art_Story', on_delete= models.CASCADE, primary_key= True)


    def __str__(self) -> str:
        return self.art_object.name

class Chariot(models.Model):
    object_number = models.IntegerField(null=True,blank=True)
    chassis_number = models.CharField(max_length=255,null=True,blank=True)
    country_of_orgin = CountryField(max_length=255,null=True,blank=True)
    reign = models.CharField(max_length=255,null=True,blank=True)
    art_object = models.OneToOneField(ArtObject, related_name='Chariot', on_delete= models.CASCADE, primary_key= True)

    def __str__(self) -> str:
        return self.art_object.name

class painting(models.Model):
    artist_name = models.CharField(max_length=255,null=True,blank=True)
    art_object = models.OneToOneField(ArtObject, related_name='Painting', on_delete= models.CASCADE, primary_key= True)

    def __str__(self) -> str:
        return self.art_object.name

class Holding(models.Model):   
    material = models.CharField(max_length=255,null=True,blank=True)

    art_object = models.ForeignKey(ArtObject, related_name='Holding', on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.art_object.name

class other(models.Model):
    object_number = models.IntegerField(null=True,blank=True)

    art_object = models.OneToOneField(ArtObject, related_name='Other', on_delete= models.CASCADE, primary_key= True)

    def __str__(self) -> str:
        return self.art_object.name

class Permenant_Collection(models.Model):
    date_aquired = models.DateTimeField(null=True,blank=True)
    art_object = models.OneToOneField(ArtObject, related_name='Permenant_Collection', on_delete= models.CASCADE, primary_key= True)

    def __str__(self) -> str:
        return self.art_object.name

class Borrowed_Collection(models.Model):
    date_borrowed = models.DateTimeField(null=True,blank=True)
    date_returned = models.DateTimeField(null=True,blank=True)
    art_object = models.OneToOneField(ArtObject, related_name='Borrowed_Collection', on_delete= models.CASCADE, primary_key= True)

    def __str__(self) -> str:
        return self.art_object.name
