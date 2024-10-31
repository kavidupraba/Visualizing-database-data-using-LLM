import sqlite3 as sq

conn=sq.connect("sample_database.db")

cursor=conn.cursor()

cursor.execute('''INSERT INTO TEST(Product_name,Amount_sold,Sale_date)
                  VALUES ('Laptop', 10, '2024-10-15'),
                         ('Smartphone', 20, '2024-10-16'),
                         ('Headphones', 15, '2024-10-17');
''')
cursor.execute('''
INSERT INTO CUSTOMERS (CUSTOMER_NAME, EMAIL, PHONE_NUMBER)
VALUES 
    ('Alice Johnson', 'alice@example.com', '1234567890'),
    ('Bob Smith', 'bob@example.com', '0987654321'),
    ('Charlie Brown', 'charlie@example.com', '1122334455');
''')

cursor.execute('''
INSERT INTO ORDERS (PRODUCT_ID, CUSTOMER_ID, QUANTITY, ORDER_DATE)
VALUES 
    (1, 1, 2, '2024-10-18'),  -- Alice ordered 2 Laptops
    (2, 2, 1, '2024-10-19'),  -- Bob ordered 1 Smartphone
    (3, 3, 3, '2024-10-20');  -- Charlie ordered 3 Headphones
''')

cursor.execute('''
INSERT INTO INVOICE (ORDER_ID, TOTAL_AMOUNT, INVOICE_DATE)
VALUES 
    (1, 2000.00, '2024-10-18'),  -- Invoice for Alice's order
    (2, 999.99, '2024-10-19'),   -- Invoice for Bob's order
    (3, 300.00, '2024-10-20');   -- Invoice for Charlie's order
''')

cursor.execute('''INSERT INTO SUPPLIERS(SUPPLIER_NAME, CONTACT_INFO)
                  VALUES ('TechSource', 'techsource@example.com'),
                         ('MobileHub', 'mobilehub@example.com'),
                         ('AudioWorld', 'audioworld@example.com');
''')


cursor.execute('''INSERT INTO EMPLOYEES(EMPLOYEE_NAME, POSITION, HIRE_DATE)
                  VALUES ('John Doe', 'Sales Manager', '2023-01-15'),
                         ('Jane Smith', 'Customer Support', '2023-06-20'),
                         ('David Black', 'Warehouse Manager', '2022-11-05');
''')


cursor.execute('''INSERT INTO PAYMENTS(INVOICE_ID, PAYMENT_DATE, AMOUNT_PAID, PAYMENT_METHOD)
                  VALUES (1, '2024-10-19', 2000.00, 'Credit Card'),
                         (2, '2024-10-20', 999.99, 'Bank Transfer'),
                         (3, '2024-10-21', 300.00, 'Cash');
''')
conn.commit()
conn.close()

print("done")