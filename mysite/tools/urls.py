from django.urls import path
from . import views
urlpatterns = [
    path('',views.tools),
    path('title_generator/',views.title_generator)
]