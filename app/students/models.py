from django.db import models

class StudentModel(models.Model):

    name = models.CharField(max_length=255, blank=False)
    age = models.IntegerField(default=18, blank=False)

    def __str__(self):
        return self.name