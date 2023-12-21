import mysql.connector
import hashlib

db_ini = {
    "host" : "localhost",
    "database" : "py201",
    "user" : "py201_user",
    "port" : 3307,
    "password" : "py201_pass",
    "charset" : "utf8mb4",
    "use_unicode" : True,
    "collation" : "utf8mb4_unicode_ci"
}

def __main__() -> None:
    global db_connection
    
    try:
        db_connection = mysql.connector.connect(**db_ini)
    except mysql.connector.Error as err:
        print(err)
    else:
        print("Connection ok")
        
    create_users()
    sql = "SHOW DATABASES"
    cursor = db_connection.cursor()
    cursor.execute(sql)
    print(cursor.column_names)
    for row in cursor:
        print(row)
        
    sql = '''
    CREATE TABLE IF NOT EXISTS products (
        id BIGINT UNSIGNED DEFAULT (UUID_SHORT()),
        name VARCHAR(64) NOT NULL,
        price FLOAT NOT NULL,
        img_url VARCHAR(256) NULL 
    ) ENGINE = InnoDB, DEFAULT CHARSET = utf8mb4 COLLATE utf8mb4_unicode_ci
    '''
    try:
        cursor.execute(sql)
    except mysql.connector.Error as err:
        print(err)
    else:
        print("Create products ok")
        
    product = {
        'name' : 'Коробка 20х30х40',
        'price' : 30,
        'img_url' : 'box1.png'
    }
    add_product(**product)
    add_user("alpha", "beta")
db_connection = None

def add_product(name: str,price: float,  img_url:str|None = None):
    sql = f"INSERT INTO products (name, price, img_url) VALUES('{name}', {price}, '{img_url}')"
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql)
            db_connection.commit()
    except mysql.connector.Error as err:
        print(err)
        return
    else:
        print("INSERT INTO products ok")

def add_user(login:str, password:str, avatar:int|None = None) :
    password = hashlib.md5( password.encode() ).hexdigest()
    sql = f"INSERT INTO users (login, password, avatar) VALUES('{login}', '{password}', '{avatar}')"
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql)
            db_connection.commit()
    except mysql.connector.Error as err:
        print(err)
    else:
        print("Insert user OK")
        
def create_users() -> None:
    sql = '''
    CREATE TABLE IF NOT EXISTS users (
        id BIGINT UNSIGNED PRIMARY KEY DEFAULT (UUID_SHORT()),
        password CHAR(32) NOT NULL,
        login VARCHAR(32) NOT NULL,
        avatar VARCHAR(256) NULL
    ) ENGINE = InnoDB, DEFAULT CHARSET = utf8mb4 COLLATE utf8mb4_unicode_ci
    '''
    cursor = db_connection.cursor()
    cursor.execute(sql)

if __name__ == "__main__":
    __main__()