from rest_framework import serializers
from .models import CollaboratorModel


class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaboratorModel
        fields = '__all__'
        # fields = ['id', 'user']
