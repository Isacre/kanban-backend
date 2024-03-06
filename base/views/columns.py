from rest_framework import viewsets
from base.models.column import Column
from base.serializers.column_serializer import ColumnSerializer

class ColumnsViewset(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = []
    

