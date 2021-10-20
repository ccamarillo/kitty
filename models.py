from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, Enum
from sqlalchemy.orm import backref, relationship
import enum

# A large project that can be broken into chunks
class Kit(Base):
    __tablename__ = 'kit'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class TaskStyleEnum(enum.Enum):
    saga = 'saga'
    epic = 'epic'
    story = 'story'
    subtask = 'subtask'
    
class Status(Base):
    __tablename__ = 'statuses'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Role(Base):
    __tablename__ = 'roles'
    role_id = Column(Integer, primary_key=True)
    name = Column(String)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name_first = Column(String)
    name_last = Column(String)
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    role = relationship(
        Role,
        backref=backref('roles',
                        uselist=True,
                        cascade='delete,all'))


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    kit_id = Column(Integer, ForeignKey('kit.id'))
    kit = relationship(
        Kit,
        backref=backref('tasks',
                        uselist=True,
                        cascade='delete,all'))
    style = Column(Enum(TaskStyleEnum))
    status_id = Column(Integer, ForeignKey('statuses.id'))
    status = relationship(
        Status,
        backref=backref('statuses',
            uselist=True,
            cascade='delete,all'))
    created_by_id = Column(Integer, ForeignKey('user.id'))
    created_by = relationship(
        User,
        backref=backref('created_by',
            uselist=True,
            cascade='delete,all'))
    # assignee_id = Column(Integer, ForeignKey('user.id'))
    # assignee = relationship(
    #     User,
    #     backref=backref('assignee',
    #         uselist=True,
    #         cascade='delete,all'))





