from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional django view',
            'Gives you the most control over your app logic',
            'Is mapped manually to URls',
        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})
        
    def post(self, request):
        """Creates a hello message with name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """Handles partial update of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'uses actions (list, create, retreive, update, partial_uodate)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]
        
        return Response({'message':'Hello!', 'a_viewset':a_viewset})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)