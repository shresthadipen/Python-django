"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog, name = 'blog'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/<int:id>/edit/', views.blog_update, name='blog_update'),
    path('blog/<int:id>/delete/', views.blog_delete, name='blog_delete'),

    path('student_list/', views.student_list, name='student_list'),
    path('student_create/', views.student_create, name='student_create'),

    path('customer_list/', views.customer_list, name='customer_list'),
    path('customer_create/', views.customer_create, name='customer_create'),

    
]
