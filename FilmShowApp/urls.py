from django.urls import path
from .views import UploadVideo, GetVideo, GetStreamingVideo, UpdateVideo

urlpatterns = [
    path("upload/", UploadVideo.as_view()),
    path("list/", GetVideo.as_view()),
    path("update/<int:pk>/", UpdateVideo.as_view()),
    path("videos/<int:id>/stream/",
         GetStreamingVideo.as_view(), name='video-stream'),
]
