from django.contrib.auth import views as auth_views
from django.urls import path
# from django.views.i18n import set_language
from django.conf.urls.i18n import set_language

from . import views
from .forms import LoginForm
# from .views import forgot_password
from django.views.i18n import set_language



# from django.urls import path
# from .views import (
#     ItemDetailView,
#     CheckoutView,
#     HomeView,
#     OrderSummaryView,
#     add_to_cart,
#     remove_from_cart,
#     remove_single_item_from_cart,
#     PaymentView,
#     AddCouponView,
#     RequestRefundView
# )



app_name = 'core'

urlpatterns = [


    path('i18n/', set_language, name='set_language'),
    path('setlang/', set_language, name='set_language'),
    # path('i18n/', set_language('django.conf.urls.i18n')),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    # path('profile/<str:pk>', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),  
    path('logout/', views.logout , name='logout'),
    path('forgot_password/', views.forgot_password , name='forgot_password'),

                    # <span class="badge red z-depth-1 mr-1"> {{ request.user|cart_item_count }} </span>


    # path('', HomeView.as_view(), name='home'),
    # path('checkout/', CheckoutView.as_view(), name='checkout'),
    # path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    # path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    # path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    # path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    # path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    # path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
    #      name='remove-single-item-from-cart'),
    # path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    # path('request-refund/', RequestRefundView.as_view(), name='request-refund')


]

