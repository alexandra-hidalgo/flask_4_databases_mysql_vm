from flask import Flask, render_template
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)

# # Create a SQLite database (you can change this to your specific database)
DATABASE_URL = "mysql+pymysql://alexa:barranquillera22@20.25.78.10:3306/alexandra"
# DATABASE_URL = "mysql+mysqlconnector://hants:INSERT-HERE@scratch-server.mysql.database.azure.com/hants"


app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

# Create a SQLAlchemy engine and session
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    # Retrieve data from the database
    query = text("select * from Clients;")    
    Clients = session.execute(query).all()
    return render_template('index.html', Clients=Clients)

if __name__ == '__main__':
    app.run(debug=True)


