from rest_framework import serializers
from watchlist_app.models import Movie

# Model serializer
class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

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

