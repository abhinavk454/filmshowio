from .models import Video
from .serializers import VideoSerializers
from rest_framework import generics
from django.http import StreamingHttpResponse


class UploadVideo(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers


class GetVideo(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers


class GetStreamingVideo(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    lookup_field = 'id'
    serializer_class = VideoSerializers

    def get(self, request, *args, **kwargs):
        video = self.get_object()
        video_file = video.file

        def stream_file(file):
            with open(file.path, 'rb') as f:
                while True:
                    chunk = f.read(1024)
                    if not chunk:
                        break
                    yield chunk

        response = StreamingHttpResponse(stream_file(video_file))
        response['Content-Type'] = 'video/x-matroska'
        response['Content-Length'] = video_file.size
        return response
