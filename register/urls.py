from django.urls import path
from .views import RegisterView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'register'

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
