from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include(('basics.urls'), namespace='todos')),
    path('csv-downloader/', include('csv_downloader.urls'))
]
