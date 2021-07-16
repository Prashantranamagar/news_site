from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('news.urls')),
    path('', include('category.urls')),
    path('', include('subcategory.urls')),
    path('', include('contactform.urls')),
    path('', include('trending.urls')),
    path('', include('manager.urls')),
    path('', include('comments.urls')),
    path('', include('newsletter.urls')),








]


if settings.DEBUG:

	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
