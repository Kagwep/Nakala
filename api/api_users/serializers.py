
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','phone_number','password')
        extra_kwargs = {'password': {'write_only': True}}

 