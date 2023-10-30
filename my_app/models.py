from django.db import models

 

class Our_Services(models.Model):
    name = models.CharField(max_length=255,verbose_name='servis adi',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='media/',null=True,blank=True)

    def __str__(self):

     return self.name
    
    class Meta:
       ordering = ('name',) 
       verbose_name = 'servis'
       verbose_name_plural = 'servisler'

class Portfolio(models.Model):
    image = models.ImageField(upload_to='media/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
  
    