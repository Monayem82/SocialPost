from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path,include
from django.contrib.auth.urls import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('twieetpost/', include('twieetPost.urls')),
    #path('twieetpost/', include('django.contrib.auth.urls')),

]


if settings.DEBUG:
 urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
