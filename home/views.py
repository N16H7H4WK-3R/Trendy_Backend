from rest_framework.decorators import api_view
from rest_framework.response import Response

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
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
