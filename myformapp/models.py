from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length = 64)
    last_name = models.CharField(max_length = 64)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length = 12)
    
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    class Meta:
        ordering = ['first_name']