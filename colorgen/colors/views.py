from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer, UserLoginSerializer, ColorHashSerializer
from .models import ColorHash
from rest_framework import generics

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"id": user.id, "username": user.username, "email": user.email}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        tokens = serializer.validated_data
        return Response(tokens, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def color_hash_list_create(request, id=None):
    if id:  # If an ID is provided, fetch the specific color hash
        color_hash = get_object_or_404(ColorHash, id=id, user=request.user)
        if request.method == 'GET':
            serializer = ColorHashSerializer(color_hash)
            return Response(serializer.data)

    if request.method == 'GET':
        color_hashes = ColorHash.objects.filter(user=request.user)
        serializer = ColorHashSerializer(color_hashes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ColorHashSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def color_hash_update(request, id):
    print('color_hash_update')
    """Update a specific ColorHash by ID."""
    color_hash = get_object_or_404(ColorHash, id=id, user=request.user)
    
    serializer = ColorHashSerializer(color_hash, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)