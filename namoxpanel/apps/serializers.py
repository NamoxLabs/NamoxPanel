from rest_framework import serializers

from .models import App as AppModel
from namoxpanel.utils import get_request_token


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppModel
        fields = '__all__'

    @get_request_token
    def create(self, validated_data):
        if validated_data['created_by']:
            category_obj = AppModel.objects.create(**validated_data)
            return category_obj
