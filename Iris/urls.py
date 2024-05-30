from django.contrib import admin
from django.urls import path

from Basics.views import Home  # Update import statement here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', Home, name='Home'),  # Note the trailing slash here
]



from django.urls import path
from django.views.generic import RedirectView

from Basics.views import Home

urlpatterns = [
    path('', RedirectView.as_view(url='Home/', permanent=False)),
    path('admin/', admin.site.urls),
    path('Home/', Home, name='Home'),
]
