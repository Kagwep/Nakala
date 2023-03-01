from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .serializers import UserSerializer

#get all users / post new user
class UserList(APIView):

    def get(self, request):
        #get all users from model
        users = User.objects.all()
        #serialize our user objects
        serializer = UserSerializer(users, many=True)
        #return serialized data
        return Response(serializer.data)

    def post(self, request):
        #use our serializer class to serialize data from request
        serializer = UserSerializer(data=request.data)
        #if valid
        if serializer.is_valid():
            #save object
            serializer.save()
            #return the data 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #if not return status and the reason
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

    # Retrieve, update or delete a user instance

    #get user
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404
        
     #get user by id
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

 
    #update the fields of requested object id
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

        #save the update
        user.save()

         #serialize the user
        serializer = UserSerializer(user)
         # return the updated data
        return Response(serializer.data)

    #get the user by id
    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        #delete the user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
