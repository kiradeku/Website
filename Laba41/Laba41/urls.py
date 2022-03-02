"""
Definition of urls for Laba41.
"""

from datetime import datetime
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('link/', views.link, name='link'),
    path('anketa/', views.anketa, name='anketa'),
    path('registration/', views.registration, name='registration'),
    path('blog/', views.blog, name='blog'),
    path('(?P<parametr>\d+)', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('videopost', views.videopost, name='videopost')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()