import mysql.connector
import MySQLdb
from sqlalchemy import create_engine

def dbconnect():

    config = {
        'host': 'MASK',
        'user': 'MASK',
        'password': 'MASK',
        'database': 'MASK',
        'port': 'MASK',
        }

    cnx = mysql.connector.connect(**config)
    return cnx

def alchemyConnect():
    connect = 'MASK'
    engine = create_engine(connect)
    return engine


def main():
    alchemyConnect()
    dbconnect()



if __name__ == "__main__":
  main()
