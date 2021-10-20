from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Kit, Task, User, Role, Status
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures

    # Kits
    starship = Kit(name='Starship')
    db_session.add(starship)

    # Status
    ready = Status(name='Ready')
    db_session.add(ready)
    in_progress = Status(name='In Progress')
    db_session.add(in_progress)
    complete = Status(name='Complete')
    db_session.add(complete)
    blocked = Status(name='Blocked')
    db_session.add(blocked)
    manager = Role(name='manager')
    db_session.add(manager)
    engineer = Role(name='engineer')
    db_session.add(engineer)

    peter = User(
        name_first='Peter', 
        name_last="Jones", 
        role=engineer
    )
    db_session.add(peter)
    roy = User(
        name_first='Roy', 
        name_last="Rogers", 
        role=engineer
    )
    db_session.add(roy)
    tracy = User(
        name_first='Tracy', 
        name_last="Grogan", 
        role=manager
    )
    db_session.add(tracy)

    # Tasks
    gut_interior = Task(
        name='Gut Interior', 
        kit=starship, 
        style='saga', 
        created_by=peter
    )
    db_session.add(gut_interior)

    db_session.commit()
