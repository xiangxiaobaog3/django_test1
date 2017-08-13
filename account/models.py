# -*- coding: utf-8 -*-
from django.db import models
from account.myauth import UserProfile
# Create your models here.

class UserType(models.Model):
	
	name = models.CharField(max_length=50)


class Group(models.Model):
	
	Name = models.CharField(max_length=50)
	
	
class UserInfo(models.Model):
	
	username = models.CharField(max_length=50)
	
	password = models.CharField(max_length=50)
	
	typeId = models.ForeignKey(UserType, verbose_name='用户类型')
	
	group_relation = models.ManyToManyField(Group, verbose_name='用户所数组')