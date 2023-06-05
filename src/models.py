import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__= "user"
    id = Column(Integer, primary_key = True)
    email = Column(String(30), nullable = False, unique = True)
    username = Column(String(30), nullable = False , unique = True)
    password = Column(String(30), nullable = False)
    favorites = relationship("favorite")

class Character (Base):
    __tablename__= "character"
    id = Column(Integer, primary_key = True)
    name = Column(String(40), nullable = False)
    birth_year = Column(String(30), nullable = True)
    height = Column(String(30))
    skin_color = Column(String(15))
    faction = Column(String(50))
    origin_planet = Column(String(30))
    favorites = relationship("favorite")

class Planet (Base):
    __tablename__="planet"
    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False)
    surface = Column(String(20))
    population = Column(Integer)
    faction = Column(String(50)) 
    favorites = relationship("favorite")

class Favorite (Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key = True)

    character_id = Column(Integer, ForeignKey("character.id"), nullable = True)
    character = relationship(Character)

    planet_id = Column(Integer, ForeignKey("planet.id"), nullable = True)
    planet = relationship(Planet)

    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    user = relationship(User)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
