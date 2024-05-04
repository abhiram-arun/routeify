from rest_framework import serializers
from .models import Users,Buses

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('ID','LOCATION','QRDECODE')
        
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('ID','LOCATION','QRDECODE')