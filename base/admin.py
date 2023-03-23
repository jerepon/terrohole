from django.contrib import admin
from .models import Post,Comment
from .models import ContactForm
from .models import Pelicula
from .models import HorrorStory
# Register your models here.
admin.site.register(Post),
admin.site.register(Comment),
admin.site.register(ContactForm)

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'director', 'duracion')

class HorrorStoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(HorrorStory, HorrorStoryAdmin)