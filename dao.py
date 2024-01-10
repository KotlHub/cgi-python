import logging
import sys
sys.path.append('../') # додати папку пошуку модулів
import db_ini
import mysql.connector

def get_db():
    return mysql.connector.connect(**db_ini.connection_params)

class Products :
    def get_all(self) :
        sql = "SELECT * FROM products"
        res = []
        try:
           db = get_db()
           with db.cursor() as cursor:
              cursor.execute(sql)
              for row in cursor:
                res.append(dict(zip(cursor.column_names,map(str,row))))
        except mysql.connector.Error as err:
            logging.error('DAO product', {'sql': sql, 'err': err})
            raise RuntimeError
        except Exception as ex:
            logging.error('DAO product', {'sql': sql, 'ex': ex})
            raise RuntimeError
        else:
            return res
        
class Auth:
    def get_user_id(token:str) -> str | None:
        sql = "SELECT COUNT(id) FROM users WHERE id=?"
        try:
           db = get_db()
           with db.cursor() as cursor:
              cursor.execute(sql)
              cnt = cursor.fetchone()[0]
        except mysql.connector.Error as err:
            logging.error('DAO product', {'sql': sql, 'err': err})
            raise RuntimeError
        except Exception as ex:
            logging.error('DAO product', {'sql': sql, 'ex': ex})
            raise RuntimeError
        else:
            return token if cnt == 1 else 0