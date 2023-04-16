from datetime import datetime

from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from .forms import *

urlpatterns = [
    path('', Home.as_view(), name='home'), 
    path('about/', About.as_view(), name='about'), 
    path('contact/', Contact.as_view(), name='contact'),
    path('admin/', admin.site.urls),
    path('add_award/', AddAward.as_view(), name='add_award'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)