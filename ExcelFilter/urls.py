"""lmlvespa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from ExcelFilterapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
        path('view_data/', views.view_data),
                path('home/', views.home),

        path('load_data/',views.load_data),
        path('top-parent-view/', views.top_parent_view, name='top_parent_view'),
        path('children-view/', views.children_view, name='children_view'),

        path('top-parent/', views.top_parent, name='top_parent'),
        path('children/', views.children, name='children'),
        path('active-inactive-count/', views.active_inactive_count),
        path('avg_price/',views.avg_price)

]
