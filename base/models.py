from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='static/images', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text=models.TextField()
    user=models.ForeignKey(User,null=True ,on_delete=models.SET_NULL)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
     


class Usuario(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    genero = models.CharField(max_length=50)
    director = models.CharField(max_length=100)
    actores = models.TextField()
    clasificacion = models.CharField(max_length=10)
    duracion = models.IntegerField()
    imagen = models.ImageField(upload_to='static/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

class HorrorStory(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)