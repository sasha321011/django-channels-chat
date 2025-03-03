import jwt
from django.contrib.auth import get_user_model
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from datetime import datetime, timedelta, timezone


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = self.extract_token(request=request)
        if token is None:
            return None

        try:
            payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
            self.verify_token(payload=payload)

            user_id = payload['id']
            user = get_user_model().objects.get(id=user_id)
            return (user,token)
        except (InvalidTokenError,ExpiredSignatureError,get_user_model().DoesNotExist):
            raise AuthenticationFailed('Invalid Token')



    def verify_token(self,payload):
        if 'exp' not in payload:
            raise InvalidTokenError('Token is no available')

        exp_timestamp = payload['exp']
        current_time = datetime.now(timezone.utc).timestamp()
        if current_time > exp_timestamp:
            raise ExpiredSignatureError('Token is not available')


    def extract_token(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer'):
            return auth_header.split(' ')[1]
        return None

    @staticmethod
    def generate_token(payload):
        expiation = datetime.utcnow() + timedelta(hours=24)
        payload['exp'] = expiation
        token = jwt.encode(payload=payload,key=settings.SECRET_KEY,algorithm='HS256')
        return token

