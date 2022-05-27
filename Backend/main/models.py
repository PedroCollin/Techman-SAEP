from django.db import models

class UserTech(models.Model):
    name = models.CharField(max_length=50)
    password = models.IntegerField()

    def __str__(self):
        return self.name

def upload_device_image(instance, filename):
    return f"{instance.id}-{filename}"

class Devices(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    image = models.FileField(upload_to=upload_device_image)

    def __str__(self):
        return self.name
    

class Comments(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=1000)
    userFK = models.ForeignKey(UserTech, on_delete=models.CASCADE)
    deviceFK = models.ForeignKey(Devices, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description

