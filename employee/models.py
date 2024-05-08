from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    job_title = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="images", default="images/default_image.jpg")

    def __str__(self):
        return f"{self.name} - {self.department}"