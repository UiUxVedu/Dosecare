from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    relation = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class PatientProfile(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ ADD THIS

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    disease = models.CharField(max_length=100)
    weight = models.FloatField()
    symptoms = models.TextField()
    medication_duration = models.CharField(max_length=100)

    def __str__(self):
        return self.nam