'''
import mysql.connector
def local():
    local_db = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="root",
                        database="jspbol"

                                            )
    return local_db
'''
import pymysql
def local():
    local_db = pymysql.connect(
                        host="localhost",
                        user="root",
                        password="root",
                        database="jspbol"

                                            )
    return local_db
