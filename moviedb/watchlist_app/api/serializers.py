from rest_framework import serializers

# Regular Serializer
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()