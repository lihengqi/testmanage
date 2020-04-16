"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from djangotest import views
from autotest import view
from product import product_views
from apitest import views
from bug import views as bug_views
from set import views as set_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test/', views_api.test),
    # path("django/", views.djangotest),
    path("login", view.login),
    path("home/", view.home),
    path("logout/", view.logout),
    path("product_manage", product_views.product_manage),
    path("apitest_manage", views.apitest_manage),
    path("apistep_manage", views.apistep_manage),
    path("apis_manage", views.apis_manage),
    path("bug_manage", bug_views.bug_manage),
    path("set_manage", set_views.set_manage),
    path("user", set_views.set_user)
]
