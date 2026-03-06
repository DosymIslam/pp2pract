import re
import json

# read file
with open("raw.txt", "r") as file:
    text = file.read()

# Extract prices
prices = re.findall(r"\d+\.\d{2}", text)

# Extract products (word + price)
products = re.findall(r"([A-Za-z]+)\s+(\d+\.\d{2})", text)

# Extract date
date = re.search(r"\d{2}/\d{2}/\d{4}", text)

# Extract time
time = re.search(r"\d{2}:\d{2}", text)

# Extract payment method
payment = re.search(r"Payment Method:\s*(\w+)", text)

# Convert prices to float
prices_float = [float(p) for p in prices]

# Calculate total
total = sum(prices_float)

# Create structured data
receipt = {
    "date": date.group() if date else None,
    "time": time.group() if time else None,
    "products": [
        {"name": name, "price": float(price)}
        for name, price in products
    ],
    "total": round(total, 2),
    "payment_method": payment.group(1) if payment else None
}

#Print JSON result
print(json.dumps(receipt, indent=4))