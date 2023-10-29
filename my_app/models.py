from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=255,verbose_name='cateqoriya adi')



    def __str__(self):

     return self.name
    
    class Meta:
       ordering = ('name',)
       verbose_name = 'cateqoriya adi'
       verbose_name_plural = 'cateqoriya adlari'

class Our_Services(models.Model):
    name = models.CharField(max_length=255,verbose_name='cateqoriya adi',null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):

     return self.name
    
    class Meta:
       ordering = ('category',) 
       verbose_name = 'servis'
       verbose_name_plural = 'servisler'

class CategoryImage(models.Model):
    our_service = models.ForeignKey(Our_Services,on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(upload_to='media/')


    def __str__(self):

     return self.our_service.name
    