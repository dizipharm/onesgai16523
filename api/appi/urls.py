from django.urls import include, path
# from rest_framework import routers
from appi import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

from django.urls import path,include
from .views import *
from django.conf.urls import *


urlpatterns=[

    path('builder/', BuildersAPIView.as_view(),name='carbon_input_list'),
    path('builder/<int:id>/', BuildersAPIView.as_view(),name='carbon_input_operation'),

    path('suppliers/', SupplierAPIView.as_view(), name='suppliers-api'),
    path('suppliers/<int:pk>/', SupplierAPIView.as_view(), name='suppliers-detail-api'),
]
    