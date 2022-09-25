from rest_framework import serializers
# from .models import Project
from .models import nurse, doctor, patient, kindred, medical_history, assistant, user

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = nurse
        fields = '__all__'
        read_only_fields = ('created_at',)

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = '__all__'
        read_only_fields = ('created_at',)

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = '__all__'
        read_only_fields = ('created_at',)

class KindredSerializer(serializers.ModelSerializer):
    class Meta:
        model = kindred
        fields = '__all__'
        read_only_fields = ('created_at',)

class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = medical_history
        fields = '__all__'
        read_only_fields = ('created_at',)

class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = assistant
        fields = '__all__'
        read_only_fields = ('created_at',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = user
      fields = '__all__'
      read_only_fields = ('created_at',)
