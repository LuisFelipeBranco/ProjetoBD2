from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('consulta/', include('consulta.urls')),
    path('admin/', admin.site.urls),
]