from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .serializers import UserSerializer

class UserList(APIView):
    """
    List all users or create a new user
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance
    """
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # def put(self, request, pk):
    #     user = User.objects.get(id=pk)
    #     serializer = UserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     print(serializer.errors)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        user = User.objects.get(id=pk)

        # Only update fields that were provided
        if 'username' in request.data:
            user.username = request.data['username']
        if 'email' in request.data:
            user.email = request.data['email']
        if 'first_name' in request.data:
            user.first_name = request.data['first_name']
        if 'last_name' in request.data:
            user.last_name = request.data['last_name']
        if 'phone_number' in request.data:
            user.phone_number = request.data['phone_number']

        user.save()

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
