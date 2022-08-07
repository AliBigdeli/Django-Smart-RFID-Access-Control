from rest_framework import serializers
from rest_framework import status
from ..models import *
class GatewayCardReaderSerializer(serializers.Serializer):
    card_reader = serializers.CharField(required=True)
    card_id = serializers.CharField(required=True)


class CardReaderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReaderGateway
        fields = [
            "id",
            "name",
            "gateway_id",
            "created_date",
            "updated_date"
        ]
        
    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
        
class CardUidSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=UIDCard
        fields = [
            "id",
            "name",
            "gateway",
            "access",
            "card_id",
            "created_date",
            "updated_date"
            
        ]
        
    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
    
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep["gateway"] = {
            "id": instance.gateway.id,
            "name": instance.gateway.name
        }
        rep["access"] = {
            "id": instance.access,
            "name": instance.get_access_display()
        }
        return rep
        
class EventLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EventLog
        fields = [
            "id",
            "card",
            "gateway",
            "created_date"
        ]
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["gateway"] = {
            "id": instance.gateway.id,
            "name": instance.gateway.name
        }
        try:
            card_obj = UIDCard.objects.get(card_id =instance.card,gateway=instance.gateway)            
            rep["owner"] = card_obj.name
            
        except:
            rep["owner"] = None
        
        return rep