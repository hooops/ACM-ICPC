#-*-coding:utf-8-*-
from django.db import models
import sys
from sponsor.models import NewSponsor
from django.contrib.auth.models import User



class sponsor_ext(models.Model):
    po=(
        (0,u'暂无'),
        (1,u'待定'),
        (2,u'合作'),      
        (3,u'投诉'),
        (4,u'不合作'),
        (5,u'同意发布'),
      ) 
    sponsor=models.OneToOneField(NewSponsor)
    is_media=models.BooleanField(u'是否媒体合作',default=False)
    is_ticket = models.BooleanField(u'是否票务合作',default=False)
    state=models.SmallIntegerField(u'合作状态',blank=True, choices=po,default=0)
    end_time=models.DateTimeField(auto_now=True ,verbose_name=u'最后编辑时间')
    #便于编辑
    edit = \
            models.ForeignKey(User,verbose_name=u'创建编辑',blank=True,null=True,related_name='sponsor_edit')
    last_edit = \
            models.ForeignKey(User,verbose_name=u'最后编辑',blank=True,null=True,related_name='sponsor_last_edit')

    
    class Meta:
        #managed = False
        db_table = 'sys_sponsor_ext'
        verbose_name = u'主办方管理' 
        verbose_name_plural = u'主办方管理'
    def __unicode__(self):
        return self.state


class sponsor_message(models.Model):
    sponsor = models.ForeignKey(sponsor_ext,  verbose_name='主办方',related_name='message_sp')
    #便于编辑
    edit = \
            models.ForeignKey(User,verbose_name=u'创建编辑',blank=True,null=True,related_name='message_edit')
    last_edit = \
            models.ForeignKey(User,verbose_name=u'最后编辑',blank=True,null=True,related_name='message_last_edit')
    message=models.TextField(u'信息',null=True,blank=True,)

    black_message=models.TextField( null=True,blank=True, verbose_name='留言回复')
 
    
    begin_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    end_time = models.DateTimeField(auto_now=True,verbose_name='最后编辑时间')
 
    
    class Meta:
        #managed = False
        db_table = 'sys_sponsor_message'
        verbose_name = u'留言信息' 
        verbose_name_plural = u'留言信息'
        
    def __unicode__(self):
        return self.message