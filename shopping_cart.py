"""
Basit bir alışveriş sepeti uygulaması.
- Ürün ekleme, listeleme, silme
- Kupon kodu ile indirim uygulama
- Kullanıcı etkileşimli menü
"""

class CartItem: 
    discount_rate = 0.8
    item_count = 0

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu."
    
    @classmethod
    def create_item(cls, data_str):
        name, price, quantity = data_str.split(",")
        return cls(name, float(price), int(quantity))
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        CartItem.item_count += 1
    
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self, discount):
        self.price = self.price * discount


class Coupon:
    def __init__(self, code, discount):
        self.code = code
        self.discount = discount


c1 = Coupon("PYTHON1", 0.8)
c2 = Coupon("PYTHON2025", 0.7)
c3 = Coupon("PROGRAMMING", 0.9)
c4 = Coupon("TECHNOLOGY", 0.8)

item1 = CartItem("Eğitim", 30000, 4)
item2 = CartItem("Laptop", 80000, 2)
item3 = CartItem("Monitör", 6000, 2)
item4 = CartItem("Kitap", 500, 2)


class ShoppingCart:
    coupon_list = [c1, c2, c3, c4]

    def __init__(self, liste):
        self.liste = liste

    def add_item(self, item):
        self.liste.append(item)

    def display_items(self):
        for idx, i in enumerate(self.liste, start=1):
            print(f"{idx}. {i.name} - {i.price} TL x {i.quantity} adet")

    def calculate_totals(self):
        return sum([item.calculate_total() for item in self.liste])
    
    def remove_item(self, cart_item):
        self.liste = [item for item in self.liste if item != cart_item]

    def clear(self):
        self.liste = []

    @classmethod
    def get_coupons(cls):
        return [coupon.code for coupon in cls.coupon_list]
    
    @classmethod
    def get_coupon(cls, code):
        return next(filter(lambda c: c.code == code, ShoppingCart.coupon_list), None)
    
    def apply_coupon_to_item(self, index, code):
        if code not in ShoppingCart.get_coupons():
            raise ValueError(f"Geçersiz kupon kodu: {code}")
        
        coupon = ShoppingCart.get_coupon(code)
        self.liste[index].apply_discount(coupon.discount)


sc = ShoppingCart([item1, item2, item3, item4])

print("\n--- Sepetteki Ürünler ---")
sc.display_items()
print(f"Toplam Fiyat: {sc.calculate_totals()} TL\n")

secim = int(input("İndirim uygulanacak ürün numarasını seçin: ")) - 1

kupon_kodu = input("Kupon kodunu girin: ").strip()

try:
    sc.apply_coupon_to_item(secim, kupon_kodu)
    print("\nİndirim uygulandı!")
except ValueError as e:
    print(e)

print("\n--- Güncel Sepet ---")
sc.display_items()
print(f"Toplam Fiyat: {sc.calculate_totals()} TL")
