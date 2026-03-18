import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 🔹 1. Все цены
prices = re.findall(r"\d{1,3}(?: \d{3})*,\d{2}", text)

# преобразуем в числа
prices_clean = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

# 🔹 2. Названия товаров
products = re.findall(r"\d+\.\n(.+)", text)

# 🔹 3. Итог
total = re.search(r"ИТОГО:\n([\d ]+,\d{2})", text)
total_value = float(total.group(1).replace(" ", "").replace(",", ".")) if total else None

# 🔹 4. Дата и время
datetime = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})", text)
datetime_value = datetime.group(1) if datetime else None

# 🔹 5. Способ оплаты
payment = re.search(r"(Банковская карта|Наличные)", text)
payment_method = payment.group(1) if payment else None

# 🔹 результат
data = {
    "products": products,
    "prices": prices_clean,
    "total": total_value,
    "datetime": datetime_value,
    "payment_method": payment_method
}

print(json.dumps(data, indent=4, ensure_ascii=False))