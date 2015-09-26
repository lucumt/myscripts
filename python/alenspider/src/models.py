#-*- coding:utf-8 -*-
'''
Created on 2015-9-26

@author: Administrator
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,String,DateTime

Base = declarative_base()

class Thread(Base):
    __tablename__ = 'thread'

    tid = Column('id',String(36),primary_key=True)
    name = Column('name',String(100))
    url = Column('url',String(100))

    def __init__(self,tid,name,url):
        self.tid = tid
        self.name = name
        self.url = url

    def __repr__(self):
        return "<Metadata('%s','%s','%s')>" % (self.tid,self.name,self.url)
    
class Post(Base):
    __tablename__='post'
    
    postid = Column('post_id',String(20),primary_key=True)
    threadid = Column('thread_id',String(36))
    posttime = Column('post_time',DateTime)
    membername = Column('member_name',String(20))
    body = Column('body',String(1000))
    
    def __init__(self,postid,threadid,posttime,membername,body):
        self.postid = postid
        self.threadid = threadid
        self.posttime = posttime
        self.membername = membername
        self.body = body
        
    def __repr__(self):
        return "<Metadata('%s','%s','%s','%s','%s')>" % (self.postid,self.threadid,self.posttime,self.membername,self.body)