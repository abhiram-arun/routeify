from rest_framework.serializers import ModelSerializer
from .models import User,Buses,Bus1,Bus2,Bus3


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
 
class BusesSerializer(ModelSerializer):
    class Meta:
        model = Buses
        fields = '__all__'
               
class Bus1Serializer(ModelSerializer):
    class Meta:
        model = Bus1
        fields = '__all__'
        
class Bus2Serializer(ModelSerializer):
    class Meta:
        model = Bus2
        fields = '__all__'
        
class Bus3Serializer(ModelSerializer):
    class Meta:
        model = Bus3
        fields = '__all__'