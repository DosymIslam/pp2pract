import csv
from connect import connect

def insert_from_csv():

    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", newline='', encoding='utf-8') as file:

        reader = csv.DictReader(file)

        for row in reader:

            cur.execute(
                """
                INSERT INTO contacts (username, phone)
                VALUES (%s, %s)
                """,
                (row["username"], row["phone"])
            )

    conn.commit()

    cur.close()
    conn.close()

    print("CSV inserted")


def insert_from_console():

    username = input("Enter username: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO contacts (username, phone)
        VALUES (%s, %s)
        """,
        (username, phone)
    )

    conn.commit()

    cur.close()
    conn.close()

    print("Contact added")


def update_contact():

    username = input("Enter username: ")
    new_phone = input("New phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE contacts
        SET phone = %s
        WHERE username = %s
        """,
        (new_phone, username)
    )

    conn.commit()

    cur.close()
    conn.close()

    print("Updated")

def query_contacts():

    conn = connect()
    cur = conn.cursor()

    print("1 — Show all")
    print("2 — Search by name")
    print("3 — Search by phone prefix")

    choice = input("Choose: ")

    if choice == "1":

        cur.execute("SELECT * FROM contacts")

    elif choice == "2":

        name = input("Enter name: ")

        cur.execute(
            "SELECT * FROM contacts WHERE username ILIKE %s",
            ('%' + name + '%',)
        )

    elif choice == "3":

        prefix = input("Enter prefix: ")

        cur.execute(
            "SELECT * FROM contacts WHERE phone LIKE %s",
            (prefix + '%',)
        )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete_contact():

    username = input("Enter username: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM contacts
        WHERE username = %s
        """,
        (username,)
    )

    conn.commit()

    cur.close()
    conn.close()

    print("Deleted")



def menu():

    while True:

        print("\nPHONEBOOK")
        print("1 — Insert from CSV")
        print("2 — Add contact")
        print("3 — Update contact")
        print("4 — Query contacts")
        print("5 — Delete contact")
        print("0 — Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv()

        elif choice == "2":
            insert_from_console()

        elif choice == "3":
            update_contact()

        elif choice == "4":
            query_contacts()

        elif choice == "5":
            delete_contact()

        elif choice == "0":
            break


menu()