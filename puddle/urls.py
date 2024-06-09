from django.views.i18n import set_language
from django.conf.urls.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from cart import views 

from turtle import settiltangle
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from turtle import settiltangle






from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core'))
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)





# urlpatterns += i18n_patterns  [
#     path('i18n/', include('django.conf.urls.i18n')),
#     # path('dashboard/', include('dashboard.urls')),


# ]


urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # path('', include("store.urls"))
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    # path('cart/', include('cart.urls')),
    # path('shop/', include('cart.urls')),
    # path('index/', include('cart.urls')),
    # path('add_to_cart/', include('core.urls')),
    path('i18n/', set_language, name='set_language'),
    path('setlang/', set_language, name='set_language'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('cart', include('store.urls')),
    # path('cart_detail', include('cart.urls')),
    # path('add_cart', include('store.urls')),
    # path('', views.Cart, name='cart'),
    # path('add_cart/<int:item_id>/', views.add_cart, name='add_cart'),

    # path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
