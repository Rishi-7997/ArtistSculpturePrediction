from rest_framework import serializers
from .models import Sculpture

class SculptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sculpture
        fields = '__all__'