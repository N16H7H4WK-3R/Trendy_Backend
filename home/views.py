from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from home.models import Login
from home.serializer import LoginSerializer


@api_view(['GET', 'POST', 'PUT'])
def index(request):
    cources = {
        'courseName': 'python',
        'time': '10 hours',
        'user': '50'
    }
    data = request.data
    print("***********")
    print(data)
    print("***********")
    return Response(cources)


# Login Handeling

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        objs = Login.objects.all()
        serializer = LoginSerializer(objs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        # Check for unique Email
        existing_email = Login.objects.filter(
            Email=data.get('Email')).first()
        if existing_email:
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
