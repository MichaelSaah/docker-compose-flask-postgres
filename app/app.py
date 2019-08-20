from flask import Flask

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Base, User

app = Flask(__name__)

engine = create_engine('postgresql://app:local@db:5432/app')

# create_all creates tables based on the models that inherit from Base
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)

@app.route('/add-joe', methods=['GET'])
def add_joe():
    """
    Example endpoint that adds a user
    """
    session = Session()
    
    user = User()
    user.email = "joe@example.com"

    session.add(user)
    session.commit()

    return {'user': user.email}
