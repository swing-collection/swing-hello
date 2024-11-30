from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('hello/', include('swing_hello.urls')),  # Include the URLs from the swing_hello app
]
