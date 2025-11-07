from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from user_app.api.serializers import RegistrationSerializer
# from user_app import models # for using callbacks for autogenerating token

@api_view(['POST'])
def registration_view(req):
    if req.method == 'POST':
        serialized_data = RegistrationSerializer(data=req.data)
        data = {}
        if serialized_data.is_valid():
            account = serialized_data.save()
            data['username'] = account.username
            data['email'] = account.email

            # token = Token.objects.get_or_create(user=account)[0].key
            token = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(token),
                'access': str(token.access_token)
            }
        else:
            data = serialized_data.errors
        
        return Response(data)

        
@api_view(['POST'])
def logout_view(req):
    if req.method == 'POST':
        req.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
