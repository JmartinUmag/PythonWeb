from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base=declarative_base()

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String(32),nullable=False)
    fullname=Column(String(64),nullable=False)
    enabled=Column(Boolean,default=True)

    posts=relationship('Post',back_populates='user')#Se crea una relacion entre la clase Post y la clase User esta es 1 a muchos
    #Backpopulates indica la contraparte de la relacion

    def __repr__(self):
        return f"<User(name='{self.username}')>"

class Post(Base):#Un usuario puede tener muchos posts
    __tablename__='posts'
    id=Column(Integer,primary_key=True)
    title=Column(String(64),nullable=False)
    content=Column(String(256),nullable=False)
    created_at=Column(DateTime,default=datetime.now)
    user_id=Column(Integer,ForeignKey('users.id')) 

    user=relationship('User',back_populates='posts')
    categories=relationship('Category',secondary='post_categories', back_populates='posts')#Secondary indica la tabla de relacion muchos a muchos

    def __repr__(self):
        return f"<Post(title='{self.title}')>"

class Category(Base):
    __tablename__='categories'
    id=Column(Integer,primary_key=True)
    name=Column(String(32))

    post=relationship('Post',secondary='post_categories',back_populates='categories')

    def __repr__(self):
        return f"<Category(name='{self.name}')>"#No se tiene que instanciar PostCategory debido a que se instancia en la clase Post y Category

class PostCategory(Base):#Es una relacion muchos a muchos
    __tablename__='post_categories'

    post_id=Column(Integer,ForeignKey('posts.id'),primary_key=True)
    category_id=Column(Integer,ForeignKey('categories.id'),primary_key=True)

