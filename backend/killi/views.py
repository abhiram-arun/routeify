from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,BusesSerializer,Bus1Serializer,Bus2Serializer,Bus3Serializer
from .models import User,Buses,Bus1,Bus2,Bus3

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/backend/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of posts'
        },
        {
            'Endpoint': '/backend/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single post object'
        },
        {
            'Endpoint': '/backend/create/',
            'method': 'POST',
            'body': {'body':""},
            'description': 'Creates new post with data sent in post request'
        },
        {
            'Endpoint': '/backend/id/update/',
            'method': 'PUT',
            'body': {'body':""},
            'description': 'Creates an existing post with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting post'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getUser(request):
    user = User.objects.all()
    user_serializer = UserSerializer(user, many=True)
    return Response(user_serializer.data)

@api_view(['GET'])
def getBuses(request):
    buses = Buses.objects.all()
    buses_serializer = BusesSerializer(buses, many=True)
    return Response(buses_serializer.data)

@api_view(['GET'])
def getBus1(request):
    bus1 = Bus1.objects.all()
    bus1_serializer = Bus1Serializer(bus1, many=True)
    return Response(bus1_serializer.data)

@api_view(['GET'])
def getBus2(request):
    bus2 = Bus2.objects.all()
    bus2_serializer = Bus2Serializer(bus2, many=True)
    return Response(bus2_serializer.data)

@api_view(['GET'])
def getBus3(request):
    bus3 = Bus3.objects.all()
    bus3_serializer = Bus3Serializer(bus3, many=True)
    return Response(bus3_serializer.data)



#------------------------------------------------------------------

@api_view(['GET'])
def sgetUser(request, pk):
    user = User.objects.get(name=pk)
    user_serializer = UserSerializer(user, many=False)
    return Response(user_serializer.data)

@api_view(['GET'])
def sgetBuses(request, pk):
    buses = Buses.objects.get(name=pk)
    buses_serializer = BusesSerializer(buses, many=False)
    return Response(buses_serializer.data)

@api_view(['GET'])
def sgetBus1(request, pk):
    bus1 = Bus1.objects.get(stop=pk)
    bus1_serializer = Bus1Serializer(bus1, many=False)
    return Response(bus1_serializer.data)

@api_view(['GET'])
def sgetBus2(request, pk):
    bus2 = Bus2.objects.get(stop=pk)
    bus2_serializer = Bus2Serializer(bus2, many=False)
    return Response(bus2_serializer.data)

@api_view(['GET'])
def sgetBus3(request, pk):
    bus3 = Bus3.objects.get(stop=pk)
    bus3_serializer = Bus3Serializer(bus3, many=False)
    return Response(bus3_serializer.data)

#------------------------------------------------------------------

@api_view(['POST'])
def createUser(request):
    User_data = request.data
    user = User.objects.create(
        name=User_data['name'],
        location=User_data['location'],
    )
    user_serializer = UserSerializer(user, many=False)
    return Response(user_serializer.data)

@api_view(['POST'])
def createBuses(request):
    Buses_data = request.data
    buses = Buses.objects.create(
        name=Buses_data['name'],
        start=Buses_data['start'],
        end=Buses_data['end'],
    )
    buses_serializer = BusesSerializer(buses, many=False)
    return Response(buses_serializer.data)

@api_view(['POST'])
def createBus1(request):
    Bus1_data = request.data
    bus1 = Bus1.objects.create(
        stop=Bus1_data['stop'],
        Time=Bus1_data['Time'],
        Crowd=Bus1_data['Crowd'],
    )
    bus1_serializer = Bus1Serializer(bus1, many=False)
    return Response(bus1_serializer.data)
    

@api_view(['POST'])
def createBus2(request):
    Bus2_data = request.data
    bus2 = Bus2.object.create(
        stop=Bus2_data['stop'],
        time=Bus2_data['time'],
        crowd=Bus2_data['crowd'],
    )
    bus2_serializer = Bus1Serializer(bus2, many=False)
    return Response(bus2_serializer.data)

@api_view(['POST'])
def createBus3(request):
    Bus3_data = request.data
    bus3 = Bus3.object.create(
        stop=Bus3_data['stop'],
        time=Bus3_data['time'],
        crowd=Bus3_data['crowd'],
    )
    bus3_serializer = Bus1Serializer(bus3, many=False)
    return Response(bus3_serializer.data)

#------------------------------------------------------------------

@api_view(['PUT'])
def updateUser(request,pk):
    User_data = request.data

    user = User.objects.get(name=pk)
    user_serializer = UserSerializer(user, data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
    return Response(user_serializer.data)

@api_view(['PUT'])
def createBuses(request,pk):
    buses_data = request.data
    
    buses = Buses.objects.get(name=pk)
    buses_serializer = BusesSerializer(buses, data=request.data)
    if buses_serializer.is_valid():
        buses_serializer.save()
        
    return Response(buses_serializer.data)

@api_view(['PUT'])
def createBus1(request, pk):
    bus1_data = request.data
    bus1 = Bus1.objects.get(stop=pk)
    bus1_serializer = Bus1Serializer(bus1, data=request.data)
    if bus1_serializer.is_valid():
        bus1_serializer.save()
        
    return Response(bus1_serializer.data)
    

@api_view(['PUT'])
def createBus2(request, pk):
    bus2_data = request.data
    bus2 = Bus2.objects.get(stop=pk)
    bus2_serializer = Bus1Serializer(bus2, data=request.data)
    if bus2_serializer.is_valid():
        bus2_serializer.save()
        
    return Response(bus2_serializer.data)

@api_view(['PUT'])
def createBus3(request, pk):
    bus3_data = request.data
    bus3 = Bus3.objects.get(stop=pk)
    bus3_serializer = Bus1Serializer(bus3, data=request.data)
    if bus3_serializer.is_valid():
        bus3_serializer.save()
        
    return Response(bus3_serializer.data)