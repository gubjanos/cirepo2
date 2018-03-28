import MySQLdb
def test_mysql_connection():
    db = MySQLdb.connect("127.0.0.1","root","a","mysql" )