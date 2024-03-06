from rest_framework import serializers
from base.models.column import Column

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'