import pandas as pd
import sqlite3

# Load the CSV
csv = pd.read_csv("/Users/enzowurtele/Desktop/DATABASES/Sample-Superstore.csv", encoding='latin1')

# Create DataFrames
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

products = csv[['Product ID', 'Category', 'Sub-Category', 'Product Name']].rename(
    columns={'Product ID': 'ProductID', 'Sub-Category': 'SubCategory', 'Product Name': 'ProductName'}
)

order_details = csv[['Order ID', 'Product ID', 'Sales', 'Quantity', 'Discount', 'Profit']].rename(
    columns={'Order ID': 'OrderID', 'Product ID': 'ProductID'}
)

customer_clean = customer.drop_duplicates()
addresses_cleared = addresses.drop_duplicates()
addresses_clean = addresses_cleared.copy()

addresses_clean['AddressID'] = range(1, len(addresses_clean) + 1)

merge_table = customer_clean.merge(addresses_clean, on='CustomerID', how='inner')[['CustomerID', 'AddressID']]

# Connect to SQLite database
conn = sqlite3.connect('SuperStore.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
CustomerID TEXT PRIMARY KEY,
CustomerName TEXT,
Segment TEXT
);
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Addresses (
AddressID INTEGER PRIMARY KEY AUTOINCREMENT,
CustomerID TEXT,
City TEXT,
State TEXT,
PostalCode TEXT,
Region TEXT,
PRIMARY KEY (CustomerID, City, State, PostalCode, Region),
FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID)
)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Orders (
CustomerID TEXT,
OrderID TEXT PRIMARY KEY,
OrderDate TEXT,
ShipDate TEXT,
ShipMode TEXT,
FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID)
);
''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS Products (
ProductID TEXT PRIMARY KEY,
Category TEXT,
SubCategory TEXT,
ProductName TEXT
);
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Order_details (
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

cursor.execute(''' CREATE TABLE IF NOT EXISTS Joint_table (
CustomerID TEXT,
AddressID INTEGER,
PRIMARY KEY (CustomerID, AddressID)
)
''')

customer_clean.to_sql('Customer', conn, if_exists='replace', index=False)

addresses_clean.to_sql('Addresses', conn, if_exists='replace', index=False)

orders.to_sql('Orders', conn, if_exists='replace', index=False)

products.to_sql('Products', conn, if_exists='replace', index=False)

order_details.to_sql('Order_details', conn, if_exists='replace', index=False)

merge_table.to_sql('Joint_table', conn, if_exists='replace', index=False)
