from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.create_user(username=username, password=password, is_active=True)

        return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED) 
    





       
       
       
         
     
         
        
                      
                           
                             
                                     
                                        
                                                  
                                                     
                                                       