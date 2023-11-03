from django.db import models

# Create your models here.

class Booking(models.Model):
    First_Name = models.CharField(max_length=200, null=True)
    Last_Name = models.CharField(max_length=200, null=True)
    Mobile = models.CharField(max_length=100, null=True)
    Email = models.CharField(max_length=200)
    Booking_Date = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    
    def __str__(self):
        return self.First_Name 
    
class Contact(models.Model):
    
    Name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.Name
    


class Image(models.Model):
    user_id = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.user_id
    
class Gallary_Post(models.Model):
    text_h1 = models.CharField(max_length=200)  
    text_p = models.CharField(max_length=200)  
    gallary_post_image = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.text_h1
    
    
    