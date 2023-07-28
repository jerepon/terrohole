from django.urls import path
from .import views
from .views import contact_view
from .views import HorrorStoryListView
from django.conf import settings
from django.conf.urls.static import static
from .views import HorrorStoryList, HorrorStoryDetail








urlpatterns =[
    path('',views.home),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('post/',views.post),
    path('comment/',views.comment),
    path('post/<int:id>',views.post),
    path('register',views.registerpage),
    path('login/',views.loginpage),
    path('logout/',views.logoutpage),
    path('contact/', contact_view, name='contact'),
    path('horrorstory/', HorrorStoryListView.as_view(), name='horrorstory_list'),
    path('api/horrorstory', HorrorStoryList.as_view(), name='horrorstory-list'),
    path('api/horrorstory/<int:pk>', HorrorStoryDetail.as_view(), name='horrorstory-detail'),
    
    
   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)