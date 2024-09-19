from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.home ,name ='blog-home'),
    path('about/',views.about ,name ='blog-about')
]
 