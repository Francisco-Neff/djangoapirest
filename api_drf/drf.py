from .models import User_DRF
from rest_framework import viewsets, permissions
from .serializers import UserDRFSerializer

# Create your drf here.
class UserDRF_REST(viewsets.ModelViewSet):
    queryset = User_DRF.objects.all()
    permission_classes = [permissions.AllowAny] #Indica quien tiene permisos para acceder y hacer uso de la funcionalidad
    serializer_class = UserDRFSerializer