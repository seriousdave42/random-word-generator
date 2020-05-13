from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('word_generator', views.generator),
    path('word_generator/generate', views.generate),
    path('word_generator/reset', views.reset),
]
