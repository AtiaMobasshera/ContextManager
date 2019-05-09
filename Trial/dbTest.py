import mysql.connector
import xml.etree.cElementTree as ET
from mysql.connector import Error
from mysql.connector import errorcode
from contextlib import ContextDecorator
from contextlib import contextmanager

class dbTest():

    connection = mysql.connector.connect(
            host="",
            user="adminer",
            password="",
            database="vm-automate"
        )


    @contextmanager
    def db_transaction(connection):
        cursor = connection.cursor()
        try:
            yield cursor
        except:
            connection.rollback()
            raise
        else:
            connection.commit()
            connection.close()


    with db_transaction(connection) as cursor:
        cursor.execute("select * from user")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)



if __name__ == "__main__":
    dbTest()



