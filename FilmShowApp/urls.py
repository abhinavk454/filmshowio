from django.urls import path
from .views import UploadVideo, GetVideo

urlpatterns = [
    path("upload/", UploadVideo.as_view()),
    path("list/", GetVideo.as_view()),
]
