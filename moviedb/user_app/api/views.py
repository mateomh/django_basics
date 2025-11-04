from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app.api.serializers import RegistrationSerializer
from user_app import models

@api_view(['POST'])
def registration_view(req):
    if req.method == 'POST':
        serialized_data = RegistrationSerializer(data=req.data)
        data = {}
        if serialized_data.is_valid():
            account = serialized_data.save()
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get_or_create(user=account).key
            data['token'] = token
        else:
            data = serialized_data.errors
        
        return Response(data)

        