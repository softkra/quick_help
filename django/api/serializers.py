from rest_framework import serializers
from .models import Products, Clients, Bills, BillsProducts

class ProductsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class ClientsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('document','first_name','last_name','email')

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)