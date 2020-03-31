from django.urls import path, include
from . import views
from rssapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns= {path("", views.index, name='index'),
              path('api/', views.API_objects.as_view()),
              path('api/<int:pk>/', views.API_objects_details.as_view())}

urlpatterns = format_suffix_patterns(urlpatterns)