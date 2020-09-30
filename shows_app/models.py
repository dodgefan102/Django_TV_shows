from django.db import models
import datetime

class ShowManager(models.Manager):
    def validation(self, data):
        errors={}
        for i in Shows.objects.exclude(id=data['id']):
            if data['title']==i.title:
                errors['t']='Title is already in use'
        if(len(data['title'])<1):
            errors['t']='TV show name should be at least 2 characters'
        if(len(data['net'])==0):
            errors['n']='Please input a Network'
        if(str(data['rdate'])==''):
            errors['r']='Please input a Release Date'
        if(str(data['rdate'])!=''):
            if(datetime.datetime.strptime(data['rdate'], '%Y-%m-%d').date() > datetime.date.today()):
                errors['r']='Release Date must have occurred already'
        if len(data['desc'])!=0:
            if len(data['desc'])<10:
                errors['d']='Description must be a minimum of 10 characters'
        return errors

class Shows(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    description=models.TextField(max_length=255, default='')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ShowManager()