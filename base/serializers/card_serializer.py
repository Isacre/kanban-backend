from dataclasses import fields
from rest_framework import serializers
from base.models.card import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class CreateCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['title', 'description','index', 'column']

class SwapCardIndexSerializer(serializers.ModelSerializer):
    from_index_column = serializers.IntegerField()
    to_index_column = serializers.IntegerField()
    from_index_card = serializers.IntegerField()
    to_index_card = serializers.IntegerField()
    class Meta:
        model = Card
        fields = ['from_index_column','to_index_column', 'from_index_card', 'to_index_card']
