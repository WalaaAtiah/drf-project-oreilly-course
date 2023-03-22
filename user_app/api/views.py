from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app.api.serializers import RegistrationSerializer
from user_app import models
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST', ])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'registeration successfull'
            data['username'] = account.username
            data['email'] = account.email
            
            # for JWT token
            # data['token'] = get_tokens_for_user(account)

            # for AUTH Token
            token=Token.objects.get(user=account).key
            data['token']=token

        else:
            data = serializer.errors
        return Response(data)
