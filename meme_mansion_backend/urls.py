"""
URL configuration for meme_mansion_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import *
from allAuth.views import *
from contactUs.views import *
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
router  = routers.DefaultRouter()

router.register('Home',Memereg),
router.register('category',CategoryView),
router.register('all',Memeview),
router.register('profiles',profileView),
router.register('users',userView)






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register/', UserRegistrationApiView.as_view(),name='register'),
    path('active/<uid64>/<token>/', activate),
    path('login/',UserLoginApiView.as_view(),name='login'),
    
    path('logout/',UserLogoutView.as_view(),name='logout'),
     path('api/update-profile/', UserProfileUpdateView.as_view(), name='update-profile'),
    # path('showmeme/',ShowMeme.as_view(),name = 'ShowMeme')
    

]
urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)