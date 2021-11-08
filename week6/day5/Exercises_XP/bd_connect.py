import psycopg2
from psycopg2 import OperationalError


class MenuItem():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def create_connection(db_name, db_user, db_password, db_host, db_port):
        connection = None
        try:
            connection = psycopg2.connect(
                database='menu',
                user='localhost',
                password='P0urimraph*',
                host='127.0.0.1',
                port='5432',
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        return connection

    connection = create_connection(
        "menu", "localhost", "P0urimraph*", "127.0.0.1", "5432"
    )

    def create_database(connection, query):
        connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Query executed successfully")
        except OperationalError as e:
            print(f"The error '{e}' occurred")

    def execute_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    create_item_query = """CREATE TABLE item(
                            item_id int(5) not null
                            constraint item_pk
                            primary key,
                                price int(100) not null,
                                name_item varchar(100) not null
                            )"""

    execute_query(connection, create_item_query)

    def add_item(self, u_item_id, u_price, u_item_name):
        u_item_id = input('item ID: ')
        u_price = input('Price: ')
        u_item_name = input('Name item: ')
        insert_into_item_query = """insert into menu_item(item_id, price, name_item) VALUES
                                            (?,?,?);
                                            """, (u_item_id, u_price, u_item_name)

        execute_query(connection, insert_into_item_query)
        if execute_query(True):
            print("add successfully")

    def delete_item(self, u_item_id):
        u_item_id = input('item ID: ')
        delete_item_query = """delete from menu_item where item_id="%s";
                                                    """, u_item_id

    execute_query(connection, delete_item_query)

    def update(self):
        u_item_id = input('item ID: ')
        update_item_query = """update from menu_item where item_id="%s";
                                                    """, u_item_id

        execute_query(connection, update_item_query)

    def show_user_menu(self):
        select_item_query = """select * from menu;
                                                            """

        execute_query(connection, select_item_query)

    if __name__ == '__main__':
        menu = []
        menu = """
        (a) Add an item
        (d) Delete an item
        (v) View the menu
        (e) Exit
        """

    def show_restaurant_menu():
        ans = True;
        while ans:

            print(menu)
            choice = input("Select a choice please")
            if choice in 'aA':
                add_item(u_item_id, u_price, u_item_name)
            elif choice in 'dD':
                delete_item(u_item_id)
            elif choice in 'vV':
                show_user_menu()
            elif choice in 'xX':
                quit()
            else:
                new = input('do you want to add a line in the menu ?(y/n')
                if new in 'yY':
                    item_menu = input("Which menu do you want to add ?")
                    menu.append(item_menu)
                    print(menu)

        show_restaurant_menu()
