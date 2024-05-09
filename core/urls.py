from django.contrib.auth import views as auth_views
from django.urls import path
# from django.views.i18n import set_language
from django.conf.urls.i18n import set_language

from . import views
from .forms import LoginForm
# from .views import forgot_password
from django.views.i18n import set_language

app_name = 'core'

urlpatterns = [
    path('i18n/', set_language, name='set_language'),
    path('setlang/', set_language, name='set_language'),
    # path('i18n/', set_language('django.conf.urls.i18n')),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),  
    path('logout/', views.logout , name='logout'),
    path('forgot_password/', views.forgot_password , name='forgot_password'),

]
