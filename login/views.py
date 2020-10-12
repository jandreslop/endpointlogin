from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import NombreUsuarioSerializer

class NombreUsuarioView(APIView):
    def post(self, request):
        nombreusuario_serializer =NombreUsuarioSerializer(data = request.data)

        if nombreusuario_serializer.is_valid():
            nombreusuario_serializer.save()
            return Response(
                nombreusuario_serializer.data, 
                status=status.HTTP_201_CREATED
            )

        else: 
            return Response(
                nombreusuario_serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )