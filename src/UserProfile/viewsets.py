from django.contrib.auth.models import User
from rest_framework import viewsets, status,mixins
from rest_framework.response import Response
from .serializers import UserSerializer,ProfileSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly,IsProfileOwnerOrReadOnly
from .models import Profile

class UserViewset(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset=User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        
        if user.temporary_password:
            return Response(
                {
                    'message': 'Registration Successful !!! Your can use following credentials to login',
                    'UserID': user.id,
                    'Username':user.username,
                    'password': user.temporary_password
                },
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        else:
            return Response(
                {'message': 'Registration Successful',
                 "Username" : user.username,
                 "UserID": user.id},
                 
                status=status.HTTP_201_CREATED,
                headers=headers
            )
    
class ProfileViewset(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrReadOnly,]

