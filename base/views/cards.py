from rest_framework import viewsets
from base.models.card import Card
from base.models.column import Column
from base.serializers.card_serializer import CardSerializer, CreateCardSerializer, SwapCardIndexSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist

class CardsViewset(viewsets.ModelViewSet):
    queryset = Card.objects.all().order_by('index')
    serializer_class = CardSerializer
    permission_classes = []
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateCardSerializer
        elif self.action == 'change_card_position':
            return SwapCardIndexSerializer
        else:
            return CardSerializer
        
    def create(self, request):
        column_id = request.data.get('column')
        data_with_index = {**request.data, 'index': Card.objects.filter(column=column_id).count()}
        serialized_data = CreateCardSerializer(data=data_with_index)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status.HTTP_400_BAD_REQUEST)
    

    @action(methods=['POST'], detail=False)
    def change_card_position(self, request):
        origin_card = Card.objects.get(column=request.data.get('from_index_column'), index=request.data.get('from_index_card'))
        try:
            destination_card = Card.objects.get(column=request.data.get('to_index_column'), index=request.data.get('to_index_card'))
            origin_card.index, destination_card.index = destination_card.index, origin_card.index
            origin_card.column, destination_card.column = destination_card.column, origin_card.column
            origin_card.save()
            destination_card.save()
            return Response("Positions swapped correctly", status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            destination_column = Column.objects.get(id=request.data.get('to_index_column'))
            origin_card = Card.objects.get(column=request.data.get('from_index_column'), index=request.data.get('from_index_card'))
            origin_card.index, origin_card.column = request.data.get('from_index_card'), destination_column
            origin_card.save()
            return Response("Card added to new position", status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)