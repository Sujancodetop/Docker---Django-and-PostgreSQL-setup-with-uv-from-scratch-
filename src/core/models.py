from django.db import models
class Actor(models.Model):
    name=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    #sunrisetrekkingshop
    released=models.DateField(null=True, blank=True)
    def __str__(self):
        return self.name
# Create your models here.
