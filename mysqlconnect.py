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
    connect = 'mysql+mysqldb://appoo:bernhard23@anmandb.cqup14elqcur.us-east-2.rds.amazonaws.com:3306/analysis'
    engine = create_engine(connect)
    return engine


def main():
    alchemyConnect()
    dbconnect()



if __name__ == "__main__":
  main()
