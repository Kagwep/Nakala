
from rest_framework import serializers
from users.models import User

#serializer class for our custome user model (table)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields from our model
        fields = ('id','username','email','first_name','last_name','phone_number','password')
        #use of password with min len of 8 enforced, make password field write only
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8 ,'error_messages': {
                    'min_length': 'Ensure password field has at least 8 characters.'
                }}}

 