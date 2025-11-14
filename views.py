from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, logout
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        login(request, user)
        return Response({
            'success': True,
            'message': 'Registration successful',
            'user': UserSerializer(user).data
        })
    return Response({
        'success': False,
        'errors': serializer.errors
    }, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
            'success': True,
            'message': 'Login successful',
            'user': UserSerializer(user).data
        })
    return Response({
        'success': False,
        'errors': serializer.errors
    }, status=400)

@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({'success': True, 'message': 'Logged out successfully'})

@api_view(['GET'])
def current_user(request):
    if request.user.is_authenticated:
        return Response({
            'success': True,
            'user': UserSerializer(request.user).data
        })
    return Response({'success': False, 'user': None})