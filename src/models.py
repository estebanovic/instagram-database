import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    content = Column(String(250))

class Likes(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)


class Followers(Base):
    __tablename__ = 'followers'

    username = Column(String(250), primary_key=True)
    Posts = Column()

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    comments_id = Column(Integer, ForeignKey('comments.id'))
    Comments = relationship(Comments)
    likes_id = Column(Integer, ForeignKey('likes.id'))
    Likes = relationship(Likes)


class Usuario(Base):
    __tablename__ = 'usuario'

    username = Column(String(250), primary_key=True)
    posts_id = Column(Integer, ForeignKey('posts.id'))
    Posts = relationship(Posts)
    followers_id = Column(Integer, ForeignKey('followers.username'))
    Followers = relationship(Followers)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e