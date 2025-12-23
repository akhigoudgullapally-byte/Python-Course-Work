# Taking inputs for YOUTUBE APP PRODUCT

product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))

categories_input = input("Enter Categories (comma-separated): ")
categories = [c.strip() for c in categories_input.split(",")]

available_stock = int(input("Enter Available Users/Slots: "))
sold_stock = int(input("Enter Used Users/Slots: "))
stock_details = (available_stock, sold_stock)

discount = float(input("Enter Discount Percentage: "))

features_input = input("Enter Product Features (comma-separated): ")
product_features = {f.strip() for f in features_input.split(",")}

supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")

supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

# 1. Using comma separation (sep=",")
print("Product ID, Name, Price:", product_id, product_name, price, sep=", ")

# 2. Using percentage formatting (% operator)
print("Product Discount: %.2f%%" % discount)

# 3. Using f-strings
print(f"Product Name: {product_name}")
print(f"Price: ₹{price:.2f}")
print(f"Discount: {discount}%")
print(f"Users Available: {available_stock} users")

# 4. Using .format() method
print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(
    supplier_details["name"],
    supplier_details["contact"],
    supplier_details["location"]
))

# Extra prints to clearly show data types
print("Categories (list):", categories)
print("Stock details (tuple):", stock_details)
print("Features (set):", product_features)
print("Supplier (dict):", supplier_details)
