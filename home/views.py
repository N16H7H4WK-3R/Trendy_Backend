from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person
from home.serializer import PeopleSerializer


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


@api_view(['GET', 'POST'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs , many = True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)