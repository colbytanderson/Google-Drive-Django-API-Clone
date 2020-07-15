from django.contrib import admin
from django.urls import path, include, register_converter

# defining url paths
adminPath = 'admin/'
authPath = 'auth/'

# urlpatterns (url paths mapped to views or other urlpatterns)
urlpatterns = [
    path(adminPath, admin.site.urls),
    path(authPath, include('apps.myauth.api.urls'))
]