import psycopg2
import psycopg2.extras
class DBhelper:
    def __init__(self) -> None:
        try:
            db_params = {
                    'dbname':"Hospital",
                    'user':"postgres",
                    'password':"password",
                    'host':"localhost",
                    'port':"5432"
                }
                
            self.connection = psycopg2.connect(**db_params)
            self.curr= self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except:
            print("Connection failed")
        else:
            print("Connected")
