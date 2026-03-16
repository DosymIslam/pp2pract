import re
import json

with open("raw.txt", "r") as file:
    data = file.read()

prices = re.findall(r'\d+\.\d{2}', data)
products = re.findall(r'([A-Za-z]+)\s\d+\.\d{2}', data)

date = re.search(r'\d{2}\.\d{2}\.\d{4}', data)
time = re.search(r'\d{2}:\d{2}', data)

payment = re.search(r'Payment method:\s(\w+)', data)

total = sum(map(float, prices))

result = {
    "products": products,
    "prices": prices,
    "date": date.group(),
    "time": time.group(),
    "payment": payment.group(1),
    "total": total
}
print(json.dumps(result, indent=4))
