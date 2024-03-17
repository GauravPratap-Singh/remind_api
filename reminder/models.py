from django.db import models

# Create your models here.

class Remind(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message