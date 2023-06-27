
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import global_settings , settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('subscriptions.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('thuto.urls')),

    path('^video/(?P<path>.*)$/', serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}),

]

urlpatterns += static(settings.MEDIA_ROOT, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
