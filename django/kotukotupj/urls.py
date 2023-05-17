from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('activity/', include('activity.urls')),
    path('categories/', include('categories.urls')),
    path('quotes/', include('quotes.urls')),
    path('badges/', include('badges.urls')),
]
