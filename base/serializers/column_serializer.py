from rest_framework import serializers
from base.models.card import Card
from base.models.column import Column
from base.serializers.card_serializer import CardSerializer

class ColumnSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()
    class Meta:
        model = Column
        fields = '__all__'
    
    def get_cards(self, obj):
        cards = Card.objects.filter(column=obj.id).order_by('index')
        serializer = CardSerializer(cards, many=True) 
        return serializer.data

class CreateColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['title','index']