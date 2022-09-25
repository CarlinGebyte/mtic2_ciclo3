from .models import nurse, doctor, patient, kindred, medical_history, assistant, user
from .serializers import NurseSerializer, DoctorSerializer, PatientSerializer, KindredSerializer, MedicalHistorySerializer, AssistantSerializer, UserSerializer
from rest_framework import viewsets, permissions

class NurseViewSet(viewsets.ModelViewSet):
    queryset = nurse.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NurseSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = doctor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PatientSerializer

class KindredViewSet(viewsets.ModelViewSet):
    queryset = kindred.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = KindredSerializer

class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = medical_history.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MedicalHistorySerializer

class AssistantViewSet(viewsets.ModelViewSet):
    queryset = assistant.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AssistantSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer