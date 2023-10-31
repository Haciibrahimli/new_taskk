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

class About(models.Model):
   name = models.CharField(max_length=255,verbose_name='basliq')
   description = models.TextField(null=True,blank=True)

   
   def __str__(self):
      return self.name
       
   class Meta:
       ordering = ('name',) 
       verbose_name = 'basliq'
       verbose_name_plural = 'basliqlar'

class Contact(models.Model):
    name = models.CharField(max_length=255,verbose_name='ad')
    mail = models.CharField(max_length=255,verbose_name='mail')
    tel = models.IntegerField(max_length=255,verbose_name='telefon nomresi')
    service = models.CharField(max_length=255,verbose_name='xidmet')
    mesage = models.CharField(max_length=255,verbose_name='mesage')


    def __str__(self):

     return self.name
    
    class Meta:
       ordering = ('name',) 
       verbose_name = 'ad'
       verbose_name_plural = 'adlar'
   

  
    