from rest_framework import viewsets
from base.models.card import Card
from base.serializers.card_serializer import CardSerializer

class CardsViewset(viewsets.ModelViewSet):
    queryset = Card.objects.all().order_by('index')
    serializer_class = CardSerializer
    permission_classes = []
    

