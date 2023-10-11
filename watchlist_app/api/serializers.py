from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField()
    time = serializers.CharField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
