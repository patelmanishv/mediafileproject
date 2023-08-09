from django.urls import path
from . import views

app_name = 'media_demo'

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
]

