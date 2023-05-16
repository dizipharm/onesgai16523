from django.contrib import admin
from django.urls import path,include
#from rest_framework import routers
from appi import views
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# router.register('singer',views.SingerViewSet,basename='singer')
# router.register('song',views.SongViewSet,basename='song')

urlpatterns = [
    path('', include('appi.urls')),
    # path('router/', include(router.urls)),
    path('admin/', admin.site.urls),
    
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]