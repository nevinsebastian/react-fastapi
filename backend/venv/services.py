import  database as _database
def create_database():
    return _database.base.create_all(bind=_database.engine)