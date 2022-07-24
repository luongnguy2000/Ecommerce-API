import json
from django.http import JsonResponse
from rest_framework import views, viewsets, generics, mixins
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import rest_framework


# Create your views here.
class RegisterView(views.APIView):
    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False, "message": f"user is created for '{serializers.data['username']}' ",
                             "data": serializers.data})
        return Response({"error": True, "message": serializers.errors, "status": status.HTTP_400_BAD_REQUEST})

class ProfileView(views.APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        try:
            query = Profile.objects.get(user=request.user)
            serializer =ProfileSerializer(query)
            response_message = {'error': True, 'data': serializer.data}
        except Exception as e:
            print(e)
            response_message = {'error': False, 'data':'Some things went wrong'}
        return Response(response_message)

class UpdateProfile(views.APIView):
    permission_classes =[IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    
    def post(self, request):
        try:
            user = request.user
            query = Profile.objects.get(user=user)
            data = request.data
            serializer = ProfileSerializer(query, data=data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return_res = {'message':'Profile is updated'}
        except Exception as e:
            print(e)
            return_res = {'message':'Something went wrong, please try again!'}
        return Response(return_res)

class UpdateUser(views.APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    
    def post(self, request):
        try:
            user = request.user
            data = request.data
            user_obj = User.objects.get(username=user)
            user_obj.first_name = data["first_name"]
            user_obj.last_name = data["last_name"]
            user_obj.email = data["email"]
            user_obj.save()
            response_data = {"error": False, "message": "User Data is Updated"}
        except Exception as e:
            print(e)
            response_data = {"error": True, "message": "User Data is not Update Try Again!!!"}
        return Response(response_data)
    