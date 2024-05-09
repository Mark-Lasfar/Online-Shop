from django.views.i18n import set_language
from django.conf.urls.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

]


urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
    path('i18n/', set_language, name='set_language'),
    path('setlang/', set_language, name='set_language'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
