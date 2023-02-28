from .models import Video
from rest_framework import serializers


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["title", "description", "file"]
