from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone 12", "+79123456789")
phone2 = Smartphone("Samsung", "Galaxy S21", "+79098765432")
phone3 = Smartphone("Xiaomi", "Mi 11", "+79987654321")
phone4 = Smartphone("Google", "Pixel 5", "+79876543210")
phone5 = Smartphone("OnePlus", "9 Pro", "+79765432109")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")