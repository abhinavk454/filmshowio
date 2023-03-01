from .models import Video
from .serializers import VideoSerializers
from rest_framework import generics
from django.http import StreamingHttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class UploadVideo(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        chunk_size = 1024 * 1024  # 1MB
        video = Video()
        video.file.save(file_obj.name, file_obj)
        with video.file.open(mode='ab') as destination:
            for chunk in file_obj.chunks(chunk_size):
                destination.write(chunk)
        video.save()
        serializer = VideoSerializers(video)
        return Response(serializer.data, status=HTTP_201_CREATED)


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
        response['Content-Type'] = 'video/mp4'
        response['Content-Length'] = video_file.size
        return response
