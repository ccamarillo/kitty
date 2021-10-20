from models import Kit as KitModel
from models import Task as TaskModel
from models import User as UserModel
from models import Role as RoleModel
from models import Status as StatusModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

class Kit(SQLAlchemyObjectType):
    class Meta:
        model = KitModel
        interfaces = (relay.Node, )

class Task(SQLAlchemyObjectType):
    class Meta:
        model = TaskModel
        interfaces = (relay.Node, )

class Status(SQLAlchemyObjectType):
    class Meta:
        model = StatusModel
        interfaces = (relay.Node, )

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )

class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allow only single column sorting
    all_users = SQLAlchemyConnectionField(
        User.connection, sort=User.sort_argument())
    # Allows sorting over multiple columns, by default over the primary key
    all_roles = SQLAlchemyConnectionField(Role.connection)
    # Disable sorting over this field
    all_kits = SQLAlchemyConnectionField(Kit.connection)
    all_tasks = SQLAlchemyConnectionField(Task.connection)
    all_statuses = SQLAlchemyConnectionField(Status.connection)


schema = graphene.Schema(query=Query)
