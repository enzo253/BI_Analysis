import pandas as pd
import sqlite3

# load csv
csv = pd.read_csv("/users/enzowurtele/desktop/DATABASES/Sample-Superstore.csv", encoding='latin1')

# Create DataFrames with proper column names
customer = csv[['Customer ID', 'Customer Name', 'Segment']].rename(
    columns={'Customer ID': 'CustomerID', 'Customer Name': 'CustomerName'}
)

addresses = csv[['Customer ID', 'City', 'State', 'Postal Code', 'Region']].rename(
    columns={'Customer ID': 'CustomerID', 'Postal Code': 'PostalCode'}
)

orders = csv[['Order ID', 'Customer ID', 'Order Date', 'Ship Date', 'Ship Mode']].rename(
    columns={'Order ID': 'OrderID', 'Customer ID': 'CustomerID',
             'Order Date': 'OrderDate', 'Ship Date': 'ShipDate', 'Ship Mode': 'ShipMode'}
)

products = csv[['Product ID', 'Product Name']].rename(
    columns={'Product ID': 'ProductID', 'Product Name': 'ProductName'}
)

product_categories = csv[['Sub-Category', 'Category']].rename(
    columns={'Sub-Category': 'SubCategory'}
)

order_details = csv[['Order ID', 'Product ID', 'Sales', 'Quantity', 'Discount', 'Profit']].rename(
    columns={'Order ID': 'OrderID', 'Product ID': 'ProductID'}
)
#just cleaning the data before populating the database as well as making sure the original addresses data isnt effected when making the joint_table via the copy function

customer_clean = customer.drop_duplicates()
addresses_cleared = addresses.drop_duplicates()
product_cat_cleared = product_categories.drop_duplicates()
product_cat_clean = product_cat_cleared.copy()
addresses_clean = addresses_cleared.copy()

product_cat_clean['CategoryCode'] = range(1, len(product_cat_clean) + 1)

addresses_clean['AddressID'] = range(1, len(addresses_clean) + 1)

merge_table = customer_clean.merge(addresses_clean, on='CustomerID', how='inner')[['CustomerID', 'AddressID']]

product_cat_clean['ProductID'] = products['ProductID']

# Connect to SQLite database
conn = sqlite3.connect('SuperStore.db')
cursor = conn.cursor()

# Create Tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customer (
    CustomerID TEXT PRIMARY KEY,
    CustomerName TEXT,
    Segment TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Addresses (
    AddressID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID TEXT,
    City TEXT,
    State TEXT,
    PostalCode TEXT,
    Region TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    CustomerID TEXT,
    OrderID TEXT PRIMARY KEY,
    OrderDate TEXT,
    ShipDate TEXT,
    ShipMode TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    ProductID TEXT PRIMARY KEY,
    ProductName TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Product_Categories (
    ProductID TEXT,
    SubCategory TEXT,
    Category TEXT,
    CategoryCode INTEGER,
    FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Order_Details (
    OrderID TEXT,
    ProductID TEXT,
    Sales REAL,
    Quantity INTEGER,
    Discount REAL,
    Profit REAL,
    FOREIGN KEY (OrderID) REFERENCES Orders (OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Joint_Table (
    CustomerID TEXT,
    AddressID INTEGER,
    PRIMARY KEY (CustomerID, AddressID),
    FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID),
    FOREIGN KEY (AddressID) REFERENCES Addresses (AddressID)
);
''')

customer_clean.to_sql('Customer', conn, if_exists='replace', index=False)

addresses_clean.to_sql('Addresses', conn, if_exists='replace', index=False)

orders.to_sql('Orders', conn, if_exists='replace', index=False)

products.to_sql('Products', conn, if_exists='replace', index=False)

order_details.to_sql('Order_Details', conn, if_exists='replace', index=False)

merge_table.to_sql('Joint_Table', conn, if_exists='replace', index=False)

product_cat_clean.to_sql('Product_Categories', conn, if_exists='replace', index=False)
