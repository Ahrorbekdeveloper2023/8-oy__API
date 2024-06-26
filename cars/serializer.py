from rest_framework import serializers
from .models import Cars
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'name', 'price', 'descriptions', 'color']
        

class CarsClass:
    def __init__(self, name, price, descriptions, color):
        self.name = name
        self.price = price
        self.desdescriptions =descriptions
        self.color = color


car_one = Cars(name='MErsides W222', price=8271, descriptions='Mersides W222 2013', color='black')

class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    descriptions = serializers.CharField(max_length=500)
    color = serializers.CharField(max_length=20)


def serialization():
    print(car_one)
    serializer = CarSerializer(car_one)
    print(serializer.data)
    json = JSONRenderer().render(serializer.data)
    print(json)


def deserialization():
    json = b'{"name":"Mersides W222", "price,:"8271", "descriptions":"Mersides W222 2013", "color":"black"}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)