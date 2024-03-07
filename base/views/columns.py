from rest_framework import viewsets
from base.models.column import Column
from rest_framework.response import Response
from rest_framework import status
from base.serializers.column_serializer import ColumnSerializer, CreateColumnSerializer


class ColumnsViewset(viewsets.ModelViewSet):
    queryset = Column.objects.all().order_by('index')
    serializer_class = ColumnSerializer
    permission_classes = []
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateColumnSerializer
        else:
            return ColumnSerializer
        
    def create(self, request):
        data_with_index = {**request.data, 'index': Column.objects.count()}
        serialized_data = CreateColumnSerializer(data=data_with_index)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status.HTTP_400_BAD_REQUEST)
    
