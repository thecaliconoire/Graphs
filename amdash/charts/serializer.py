from rest_framework import serializers
from .models import People

class PeopleSerializer(serializers.ModelSerializer):
    Group=serializers.StringRelatedField(many=True)
    class Meta:
        model = People
        fields = ('FName', 'Group', 'Connections')