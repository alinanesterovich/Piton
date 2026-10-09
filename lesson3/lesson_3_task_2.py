from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "+79001234567"),
    Smartphone("Samsung", "Galaxy S24", "+79002345678"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79003456789"),
    Smartphone("Google", "Pixel 8", "+79004567890"),
    Smartphone("Huawei", "P60 Pro", "+79005678901"),
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")