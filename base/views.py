from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Post,Comment,Pelicula
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContactFormForm
from .models import Pelicula
from django.views.generic import ListView
from .models import HorrorStory
from rest_framework import generics
from .serializers import HorrorStorySerializer








# Create your views here.
def registerpage(request):
    if (request.method=='POST'):
        username=request.POST.get('username')
        email=request.POST.get('email')
        name=request.POST.get('name')
        last_name=request.POST.get('last_name')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if (password !=confirm_password):
            messages.error(request,'Las contraseñas no coinciden')
            return redirect('/register')
        User.objects.create_user(username=username,email=email,first_name=name,last_name=last_name,password=password)
        messages.success(request,'Usuario creado exitosamente')
        return redirect('/')

    return render(request,'register.html')    

def loginpage(request):
    if(request.method == 'POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(username=username).exists():
           user=authenticate(request,username=username,password=password)
           if user is not None:
            login(request,user)
            messages.success(request,'Se inició sesión correctamente')
            return redirect('/')

        messages.error(request,"Datos incorrectos")   
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect("/")


def home(request):
    posts=Post.objects.order_by('-created')
    return render(request, 'home.html',{"posts":posts})
 

def post(request,id=None):
    if request.method=='POST':
        id=request.POST.get('id')
        if (id is None):
            post = Post.objects.create(
                title=request.POST.get('title'),
                text=request.POST.get('text'),
                user=request.user,
            )
            if request.FILES.get('image'):
                post.image = request.FILES['image']
                post.save()

            messages.success(request,'Post creado correctamente')
            return redirect('/')
        else:
            p=Post.objects.get(id=id)
            if (p.user== request.user):
                p.title=request.POST.get('title')
                p.text=request.POST.get('text')
                if request.FILES.get('image'):
                    p.image = request.FILES['image']
                p.save()
                messages.success(request,'Post editado correctamente')
                return redirect('/')
    context={}
    if id is not None:
        p= Post.objects.get(id=id)
        context['post']=p   
    return render(request, 'newpost.html',context)

def comment(request):
     p= Post.objects.get(id=request.POST.get('post'))
     Comment.objects.create(
                text=request.POST.get('text'),
                user=request.user,
                post=p
       
        )
     return redirect("/")    

def contact_view(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu formulario ha sido enviado correctamente!')
            return redirect('/')  
    else:
        form = ContactFormForm()
    return render(request, 'contact.html', {'form': form})


def peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas.html', {'peliculas': peliculas})

class HorrorStoryListView(ListView):
    model = HorrorStory
    template_name = 'horrorstory_list.html'



class HorrorStoryList(generics.ListCreateAPIView):
    queryset = HorrorStory.objects.all()
    serializer_class = HorrorStorySerializer

class HorrorStoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HorrorStory.objects.all()
    serializer_class = HorrorStorySerializer