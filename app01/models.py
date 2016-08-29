#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=64,unique=True)
    ip_addr = models.GenericIPAddressField(unique=True)
    port = models.IntegerField(default=22)
    system_type_choices = (
        ('linux',"LINUX"),
        ('win32',"Windows")
    )
    system_type = models.CharField(choices=system_type_choices,max_length=32)
    enabled = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    online_date = models.DateTimeField()
    groups = models.ManyToManyField('HostGroup') #主机组
    idc = models.ForeignKey('IDC') #机房

    def __unicode__(self):
        return self.hostname

class IDC(models.Model):
    name = models.CharField(max_length=64,unique=True)

    def __unicode__(self):
        return self.name

class HostGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=64,unique=True)
    host_groups = models.ManyToManyField('HostGroup',blank=True,null=True) #关联具体组，字段可以不选，记录可以不填
    hosts = models.ManyToManyField('Host',blank=True,null=True) #关联具体的主机

    def __unicode__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=254)
    category = models.ForeignKey('Category')
    content = models.TextField(max_length=100000)
    author = models.ForeignKey('UserProfile')
    publish_date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(max_length=500)
    head_img = models.ImageField(upload_to="statics/imgs/upload/")

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(unique=True,max_length=64)
    admins = models.ManyToManyField('Userprofile')

    def __unicode__(self):
        return self.name

class ThumbUp(models.Model):
    article = models.ForeignKey('Article')
    user = models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.article.title

class UserProfile_bbs(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    user_groups = models.ManyToManyField('UserGroup')

    def __unicode__(self):
        return self.name

class UserGroup(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    article = models.ForeignKey('Article')
    user = models.ForeignKey('UserProfile_bbs')
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=1024)
    parent_comment = models.ForeignKey('Comment',blank=True,null=True,related_name='pid')

    def __unicode__(self):
        return self.comment

















