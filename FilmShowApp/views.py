from .models import Video
from .serializers import VideoSerializers
from rest_framework import generics


class UploadVideo(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers


class GetVideo(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
