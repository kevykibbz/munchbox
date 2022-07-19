from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('installation/',include('installation.urls')),
    path('panel/', include('panel.urls')),
    path('', include('manager.urls')),
]

if not settings.DEBUG:
	urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
	urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

handler400 ='errors.views.error_400'
handler403 ='errors.views.error_403'
handler404 ='errors.views.error_404'
handler500='errors.views.error_500'