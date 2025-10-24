from rest_framework import serializers
from watchlist_app.models import Movie, Review, StreamPlatform, WatchList

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['movie']
        # fields = "__all__"


# Model serializer
class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'description', 'name', 'len_name']
        # exclude = ['active']

    def get_len_name(self, object):
        return len(object.name)

    # Field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short')
        else:
            return value
        
    # Object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError(' Name and Description must be different')
        else:
            return data


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    # Same name as the related name in the foreign key field
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"

