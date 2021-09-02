from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.DateField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.title} - {self.network} - {self.date}"
    def __str__(self):
        return f"{self.title} - {self.network} - {self.date}"