from configparser import ConfigParser
import getpass
import psycopg2



def config(filename='a3.ini', section='Settings'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


def connect():
    conn = None
    
    try:
        print('Connecting to the PostgreSQL database...')

        password= getpass.getpass()
        params = config()
        stg = "host="+params['host']+ " dbname="+params['dbname']+" user="+params['user']+" password="+password
        conn = psycopg2.connect(stg)
        cur = conn.cursor()


        while True:
            while True:
                try:
                    print("\nSelect one of the following options:")
                    print("1 - Number of distinct cities whose name starts with 'L'")
                    print("2 - Distinct countries that hosted the FIFA World Cup and how many times they hosted the tournament")
                    print("3 - Various types of tournaments played by Greece")
                    print("4 - Country with the most wins in shootouts and the number of wins")
                    print("0 - Exit", "\n")
                    user_input = int(input())
                except ValueError:
                    print("Invalid Input. Input must be an integer. Enter the correct input.")
                    continue
                if user_input not in range(0,5):
                    print("Invalid Input. Input must be between 0-4 inclusive. Enter the correct input.")
                    continue
                else:
                    break

            if user_input == 0:
                break

            if user_input == 1:
                filename = "a3.q1"
                print("\nNumber of distinct cities whose name starts with 'L': \n")
                f = open(filename, "r")
                cur.execute(f.read())
                for i in cur:
                    print(i[0])
                    

            elif user_input == 2:
                filename = "a3.q2"
                print("\nDistinct countries that hosted the FIFA World Cup and how many times they hosted the tournament: \n")
                f = open(filename, "r")
                cur.execute(f.read())
                for i in cur:
                    print(i[0].ljust(35, ' '), i[1])
                    

            elif user_input == 3:
                filename = "a3.q3"
                print("\nVarious types of tournaments played by Greece: \n")
                f = open(filename, "r")
                cur.execute(f.read())
                for i in cur:
                    print(i[0])
                   

            elif user_input == 4:
                filename = "a3.q4"
                print("\nCountry with the most wins in shootouts and the number of wins: \n")
                f = open(filename, "r")
                cur.execute(f.read())
                for i in cur:
                    print(i[0] ,i[1])
                
        
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

connect()






