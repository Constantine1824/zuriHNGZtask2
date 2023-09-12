from rest_framework.views import APIView
from .serializers import PersonSerializer
from .models import Person
from rest_framework.response import Response
from rest_framework import exceptions

class CRUDApiView(APIView):
    def get(self, request, id=None, name=None):
        if id:
            queryset = Person.objects.get(id=id)
            serializer = PersonSerializer(queryset)
            return Response(serializer.data, status=200)
        if name:
            queryset = Person.objects.get(name=name)
            serializer = PersonSerializer(queryset)
            return Response(serializer.data, status=200)
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, id=None, name=None):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        
    def put(self, request, id=None, name=None):
        if id:
            try:
                queryset = Person.objects.get(id=id)
                data = request.data['name']
                queryset.name = data
                queryset.save()
                return Response(
                    {
                        'details' : 'Updated succesfully'
                    },
                    status=201
                )
            except Person.DoesNotExist:
                raise exceptions.NotFound(detail='Person resource with the given id is not found on this resource')
    
        if name:
            try:
                queryset = Person.objects.get(name=name)
                data = request.data['name']
                queryset.name = data
                queryset.save()
                return Response(
                    {
                        'details' : 'Updated succesfully'
                    },
                    status=201
                )
            except Person.DoesNotExist:
                raise exceptions.NotFound(detail='Person resource with the given name is not found on this resource')

    def delete(self, request, id=None, name=None):
        if id:
            try:
                queryset = Person.objects.get(id=id)
                queryset.delete()
                return Response(
                    {
                        'details' : 'deleted successfully'
                    },
                    status=200
                )
            except Person.DoesNotExist:
                raise exceptions.NotFound('Person resource with the given id is not found on this server')

        if name:
            try:
                queryset = Person.objects.get(name=name)
                queryset.delete()
                return Response(
                    {
                        'details' : 'deleted successfully'
                    },
                    status=200
                )
            except Person.DoesNotExist:
                raise exceptions.NotFound('Person resource with the given name is not found on this server')
    # Create your views here.
