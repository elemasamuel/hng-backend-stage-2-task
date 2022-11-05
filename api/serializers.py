from rest_framework import serializers
from base.models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

    def to_representation(self, instance):
        if instance.operation_type == "addition":
            representation = {
            "slackUsername": "elemasamuel",
            "result": instance.x + instance.y,
            "operation_type": instance.operation_type,
        }
        elif instance.operation_type == "subtraction":
            representation = {
            "slackUsername": "elemasamuel",
            "result": instance.x - instance.y,
            "operation_type": instance.operation_type,
            }
        elif instance.operation_type == "multiplication":
            representation = {
            "slackUsername": "elemasamuel",
            "result": instance.x * instance.y,
            "operation_type": instance.operation_type,
            }
        
        return representation