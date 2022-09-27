from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=200)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    type = models.CharField(max_length=200, default='patient')
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
 
class nurse(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class doctor(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class patient(models.Model):
    nurse = models.ForeignKey(nurse, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
  
class kindred(models.Model):
    patient = models.ForeignKey(patient, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class medical_history(models.Model):
    suggestion = models.CharField(max_length=2000, null=True)
    diagnosis = models.CharField(max_length=2000, null=True)
    oximetry = models.FloatField(null=True)
    brathing_rate = models.IntegerField(null=True)
    hearth_rate = models.IntegerField(null=True)
    temperature = models.IntegerField(null=True)
    blood_pressure = models.FloatField(null=True)
    glycemia = models.FloatField(null=True)
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class assistant(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

