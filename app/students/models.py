from django.db import models

class StudentModel(models.Model):
    name = models.CharField('Name', max_length=255, blank=False)
    age = models.PositiveIntegerField('Age', default=18, blank=False)
    

    def __str__(self):
        return self.name