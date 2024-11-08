import sqlite3
import datetime

conn=sqlite3.connect("expenses.db")
cur=conn.cursor()

while True:
    print("Select an option ")
    print("1.Enter new expense ")
    print("2. View expenses summary")
    choice=int(input())
    
    if choice==1:
        date=input("Enter the date of the expense (YYYY-MM-DD): ")
        description=input("Enter the description of the expense: ")
        
        cur.execute("SELECT DISTICT category expences")
        
        categories=cur.fetchall()
        
        print("Select a category by number: ")
        for idx, category in enumerate(categories):
            print(f"{idx+1}.{category}")
        print(f"{len(categories)+1}.Create a new category ")
        
        category_choice=input()
        if category_choice==len(categories)+1:
            category=input("Enter the new category name: ")
        else:
            category=categories[category_choice-1][0]
            
        price=input("Enter the price of expences: ")
        
        cur.execute("INSERT INTO expences (Date , description , category, price) VALUES (?,?,?,?)",(date,description, category,price))
        
        conn.commit()
        
        
    elif choice==2:
        print("Select an option")
        print("1. View all expences ")
        print("2. View monthly expences by category")
        view_choice=int(input())
        if choice == 1:
            cur.execute("SELECT * FROM expences")
            expenses=cur.fetchall()
            for expence in expenses:
                print(expence)
        elif view_choice==2:
            month=input("Enter the month (MM): ")
            year=input("Enter the year (YYYY): ")
            cur.execute("""SELECT category, SUM(price) FROM expences
                        WHERE strftime('%m',Date)=? AND strftime('%Y',Date) """)
        else:
            exit()
                

    else:
        exit()