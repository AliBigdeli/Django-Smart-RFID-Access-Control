from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.



class ReaderGateway(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gateway_id = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_date',)
    

UID_ACCESS = ((1,"Authorized"),
              (2,"Unauthorized"))

class UIDCard(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gateway = models.ForeignKey(ReaderGateway,on_delete=models.CASCADE)
    access = models.IntegerField(choices=UID_ACCESS,default=1)
    card_id = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_date',)
        
class EventLog(models.Model):
    card = models.CharField(max_length=100)
    gateway = models.ForeignKey(ReaderGateway,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_date',)