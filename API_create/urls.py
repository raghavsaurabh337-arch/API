"""
URL configuration for API_create project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from API import views
from API.views import studentList,AuthAPIView,school_libraryModelview,employeeLC

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('school', views.school_libraryModelview, basename='school')
router=DefaultRouter()
router.register('product', views.productAPI, basename='product')





urlpatterns = [
    path('admin/', admin.site.urls),
    path('userApi/',AuthAPIView.as_view(),name='user'),
    path('studentApi/',views.studentList.as_view(),name='student'),
    path('studentApi/<int:pk>/',views.studentRUD.as_view(),name='student'),
    path('employeeApi/',views.employeeLC.as_view(),name='employee'),
    path('employeeApi/<int:pk>/',views.employeeRUD.as_view(),name='employee'),
    path('schoolApi/', include(router.urls)),
    path('schoolApi/<int:pk>/', include(router.urls)),
    path('schoolApi/',include('rest_framework.urls')),
    path('productApi/', include(router.urls)),
    path('productApi/<int:pk>/', include(router.urls)),
    path('productApi/',include('rest_framework.urls')),


    
]
