def count_evennumbers(array):
    even_number = 0
    for i in range(len(array)):
        if i % 2 == 0:
            even_number += 1
    return even_number
# array = [1,2,3,4,5,6]
# print(count_evennumbers(array))

def two_array(array1, array2):
    array = array1 + array2 
    result = []
    while len(array) > 0:
        nho = min(array)
        result.append(nho)
        array.remove(nho)
    return result

# array1 = [1,3,5]
# array2 = [2,4,6]
# print(two_array(array1, array2))

def twoarray(array1, array2):
    result = []
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    while i < len(array1):
        result.append(array1[i])
        i += 1
    while j < len(array2):
        result.append(array2[j])
        j += 1
    return result

# array1 = [1, 3, 5]
# array2 = [2, 4, 6]
# print(twoarray(array1, array2))

        
from abc import ABC, abstractmethod

class MonAn:
    def __init__(self, pe, price):
        self.pe = pe
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print('price can not negative ')
            self._size = 'S'
    @abstractmethod
    def pay(self):
        return self.__price
    
    def __add__(self, other):
        if isinstance(other, MonAn):
            return self.pay() + other.pay()
        else:
            return NotImplemented
    
    def __str__(self):
        return f'-{self.pe}: {self.pay()} VND'
        
class DoUong(MonAn):
    def __init__(self, pe, price, size = 'S'):
        super().__init__(pe, price)
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, new_size):
        size_at = ['S', 'M', 'L']
        if new_size in size_at:
            self.__size = new_size
        else:
            print('invalid size')

    def pay(self):
        if self.size == 'S':
            price = self.price
        elif self.size == 'M':
            price = self.price + 5000
        elif self.size == 'L':
            price = self.price + 10000
        else:
            print('ivalid size')
        return price
    
    def __str__(self):
        return f'{self.pe} -{self.size} : {self.pay()} VND'
def xuat_hoa_don(list_order, file_pe = 'hoa_don.txt'):
    total = 0
    with open(file_pe, 'w', encoding= 'utf-8') as file:
        for order in list_order:
            total += order.pay()
            file.write(f'{order}\n')
        file.write(f'Tong hoa don : {total} VND\n')
# mon1 = MonAn("Bánh Croissant", 35000)
# mon2 = DoUong("Cà phê sữa đá", 29000, size="M") # 29k + 5k = 34k
# mon3 = DoUong("Trà đào cam sả", 45000, size="L") # 45k + 10k = 55k
# tongtien = mon1 + mon2
# print(tongtien)
# gio_hang = [mon1, mon2,]
# xuat_hoa_don(gio_hang)




from abc import ABC, abstractmethod
class Sanpham(ABC):
    def __init__(self, pe, root_price):
        self.pe = pe
        self.root_price = root_price
    
    @property
    def root_price(self):
        return self.__root_price
    @root_price.setter
    def root_price(self, new_price):
        if new_price >= 0:
            self.__root_price = new_price
        else:
            print('price can not negative')
        
    @abstractmethod   
    def tinh_tien(self):
        pass

class DoAn(Sanpham):
    def __init__(self, pe, root_price):
        super().__init__(pe, root_price)

    def tinh_tien(self):
        return self.root_price
    
    def __str__(self):
        return f'{self.pe} - {self.tinh_tien()}'

class DoUong(Sanpham):
    
    def __init__(self, pe, root_price, size = 'S'):
        super().__init__(pe, root_price)
        self.size = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, new_size):
        size_in = ['S', 'M', 'L']
        if new_size in size_in:
            self.__size = new_size
        else:
            print('Invalid size')
    def __str__(self):
        return f'{self.pe} -{self.size} : {self.tinh_tien()} VND'

    def tinh_tien(self):
        if self.size == 'S':
            price = self.root_price
        elif self.size == 'M':
            price = self.root_price + 5000
        elif self.size == 'L':
            price = self.root_price + 10000
        else:
            print('Invalid size')
            return 0
        return price
    
class HoaDon:
    def __init__(self):
        self.danh_sach = []

    def them_mon(self, san_pham):
        if isinstance(san_pham, Sanpham):
            self.danh_sach.append(san_pham)
        return self.danh_sach
    def __len__(self):
        so_luong = len(self.danh_sach)
        return so_luong
    def __add__(self, other):
        if isinstance(other, HoaDon):
            tong_hd1 = 0
            tong_hd2 = 0
            for mon in self.danh_sach:
                tong_hd1 += mon.tinh_tien()
            for mon in other.danh_sach:
                tong_hd2 += mon.tinh_tien()
            return tong_hd1 + tong_hd2

    def xuat_hoa_don(self, file_pe = 'hoa_don.txt'):
        total = 0
        with open(file_pe, 'w', encoding= 'utf-8') as file:
            for mon in self.danh_sach:
               total += mon.tinh_tien()
               file.write(f'{mon}\n')
            file.write(f'Tổng hóa đơn : {total} VND')
        print('Đã xuất hóa đơn thành công')
# mon_loi_gia = DoAn("Bánh mì", -15000)
# mon_loi_size = DoUong("Trà sữa", 30000, "X")
# cf_sua = DoUong("Cà phê sữa", 29000, "M")
# banh_mi = DoAn("Bánh mì thịt", 25000)
# # print(cf_sua)
# # print(banh_mi)

# hd1 = HoaDon()
# hd1.them_mon(cf_sua)
# hd1.them_mon(banh_mi)

# print(f"Số lượng món trong HD1: {len(hd1)} món")
# hd2 = HoaDon()
# tra_cam = DoUong("Trà cam sả", 35000, "S")
# hd2.them_mon(tra_cam)
# tong_doanh_thu = hd1 + hd2
# print(f"Tổng doanh thu (HD1 + HD2): {tong_doanh_thu} VND") 
# print(f"Kiểu dữ liệu trả về: {type(tong_doanh_thu)}")
# hd1.xuat_hoa_don("hoa_don.txt")

from abc import ABC, abstractmethod
class TaiKhoan(ABC):   
    def __init__(self, chu_tai_khoan, so_du):
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du
    
    @property
    def so_du(self):
        return self.__so_du
    
    @so_du.setter
    def so_du(self, so_du_moi):
        if so_du_moi >= 0:
            self.__so_du = so_du_moi
        else:
            print('So du can not negative')
            self.__so_du = 0
    @abstractmethod
    def thanh_toan(self, so_tien):
        pass

class TaiKhoanThuong(TaiKhoan):
    def __init__(self, chu_tai_khoan, so_du):
        super().__init__(chu_tai_khoan, so_du)
    
    def thanh_toan(self, so_tien):
        if so_tien <= self.so_du:
            self.so_du = self.so_du - so_tien
            return True
        else:
            print('Tai khoan khong du tien')
            return False
        
    def __str__(self):
        return f'- {self.chu_tai_khoan} - so du: {self.so_du} VND'
    
class TaiKhoanTinDung(TaiKhoan):
    def __init__(self, chu_tai_khoan, so_du, han_muc: int):
        super().__init__(chu_tai_khoan, so_du)
        self.han_muc = han_muc

    def thanh_toan(self, so_tien):
        if self.so_du - so_tien >= - self.han_muc:
           self._TaiKhoan__so_du -= so_tien
           return True
        else:
            print('Vuot qua han muc')
            return False
    def __str__(self):
        return f'{self.chu_tai_khoan} - so du: {self.so_du} VND Han muc: {self.han_muc}'
    
class NganHang:
    def __init__(self, ten, ):
        self.ten = ten 
        self.danh_sach = []
        
    def them_tai_khoan(self, tai_khoan):
        if isinstance(tai_khoan, TaiKhoan):
            self.danh_sach.append(tai_khoan)
    def __len__(self):
        return len(self.danh_sach)
    
    def __getitem__(self, index):
        return self.danh_sach[index]
    
    def __add__(self, other):
        if isinstance(other, NganHang):
            nh1 = 0
            nh2 = 0
            for so_tien in self.danh_sach:
                nh1 += so_tien.so_du
            for so_tien in other.danh_sach:
                nh2 += so_tien.so_du
            return nh1 + nh2
    def save(self, file_pe = 'hoa_don.txt'):
        total = 0
        with open(file_pe, 'w', encoding= 'utf-8') as file:
            for so_tien in self.danh_sach:
                total += so_tien.so_du
                file.write(f'{so_tien}\n')
            file.write(f'Tong so du con lai:{total} VND')
# tk1 = TaiKhoanThuong("Nguyen Van A", 5000000)
# tk2 = TaiKhoanTinDung("Tran Thi B", 0, 20000000) 
# print(tk1)
# print(tk2)
# tk1.thanh_toan(5000000)
# print(tk1)
# tk2.thanh_toan(15000000)
# print(tk2)
# vcb = NganHang('AA')
# vcb.them_tai_khoan(tk1)
# vcb.them_tai_khoan(tk2)
# vcb.save('hoa_don.txt')
# print('Xuat file thanh cong')
from abc import ABC, abstractmethod
import random
class Seat(ABC):
    def __init__(self, seat_number, row):
        self.seat_number = seat_number
        self.row = row
        self.is_booked = False
    def book(self):
        if self.is_booked:
            raise ValueError(f'Seat {self.seat_number} is already booked')
        self.is_booked = True
    def cancel(self):
        if not self.is_booked:
            raise ValueError(f'Seat {self.seat_number} is not booked')
        self.is_booked = False
    @abstractmethod
    def caculate_price(self, quantity):
        pass
    def __str__(self):
        return f'{self.seat_number} - {self.row} - {self.is_booked}'
class StandardSeat(Seat):
    def __init__(self, seat_number, row, has_extra_legroom: bool):
        super().__init__(seat_number, row)
        self.has_extra_legroom = has_extra_legroom
    def caculate_price(self, quantity):
        price = 80000 * quantity
        if self.has_extra_legroom == True:
            price *= 1.2
        return price
class VipSeat(Seat):
    def __init__(self, seat_number, row, includes_meal: bool):
        super().__init__(seat_number, row) 
        self.includes_meal = includes_meal
    def caculate_price(self, quantity):
        price = 150000 * quantity
        if self.includes_meal == True:
            price += 50000 * quantity
        return price
class CouchSeat(Seat):
    def __init__(self, seat_number, row, num_people):
        super().__init__(seat_number, row)
        self.num_people = num_people
    def caculate_price(self, quantity):
        price = 200000 * self.num_people
        if self.num_people == 2:
            price *= 0.9
        return price
class Customer:
    def __init__(self, name):
        self.name = name
        self.customer_id = random.randint(1000, 9999)
        self.booking_history = []
    def add_booking(self, seat, quantity, price):
        self.booking_history.append((seat, quantity, price))
    def total_spent(self):
        total = 0
        for pay in self.booking_history:
            total += pay[2]
        return total
    def __str__(self):
        return f'{self.name} - {len(self.booking_history)}'
class Cinema:
    def __init__(self, name):
        self.name = name
        self.seats = []
        self.customers = []
    def add_seat(self, seat):
        self.seats.append(seat)
    def register_customer(self, customer):
        self.customers.append(customer)
    def book_seat(self, customer, seat_number, quantity):
        find_seat = None
        for record in self.seats:
            if record.seat_number == seat_number:
                find_seat = record
                break
        if find_seat is None:
            raise ValueError
        find_seat.book()
        price = find_seat.caculate_price(quantity)
        customer.add_booking(find_seat, quantity, price)
        return price
    def cancel_booking(self, seat_number):
        find_seat = None
        for record in self.seats:
            if record.seat_number == seat_number:
                find_seat = record
                break
        if find_seat is None:
            raise ValueError(f'')
        find_seat.cancel()
    def available_seats(self):
        result = []
        for i in self.seats:
            if i.is_booked == False:
                result.append(i)
        return result
    def total_revenue(self):
        total = 0
        for cus in self.customers:
            for record in cus.booking_history:
                total += record[2]
        return total
# cinema = Cinema('Rap phim')
# with open('abcd.txt', 'r', encoding= 'utf-8') as file:
#     for line in file:
#         line = line.strip()
#         if not line:
#             continue
#         values = line.split('|')
#         obj = None
#         if values[0] == 'SEAT':
#             if values[1] == 'StandardSeat':
#                 obj = StandardSeat(values[2], values[3], values[4])
#             elif values[1] == 'VipSeat':
#                 obj = VipSeat(values[2], values[3], values[4])
#             elif values[1] == 'CouchSeat':
#                 obj = CouchSeat(values[2], values[3], values[4])
#             cinema.add_seat(obj)
#         elif values[0] == 'CUSTOMER':
#             obj = Customer(values[1])
#             cinema.register_customer(obj)
#             print(f'register {obj}')
#         elif values[0] == 'BOOK':
#             for cus in cinema.customers:
#                 if cus.name == values[1]:
#                     print(cinema.book_seat(cus, values[2], int(values[3])))
#                     break
#         elif values[0] == 'CANCEL':
#             cinema.cancel_booking(values[1])
    
class BankAccount:
    def __init__(self, owner, __balance):
        self.owner = owner
        self.history = [] 
        self.balance = __balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print('Invalid balance')
    def deposit(self, amount):
        self.balance += amount
        self.history.append(f'Deposit: +{amount}')
        return self.balance
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance =self.balance - amount
            self.history.append(f'Deposit: -{amount}')
            return self.balance
        else:
            print('Invalid balance')
    def show_balance(self):
        return f'{self.owner} balance: {self.balance}' 
    def print_history(self):
        for item in self.history:
            print(item)
class SavingAccount(BankAccount):
    def __init__(self, owner,interest_rate, balance=0, ):
        super().__init__(owner, balance,)
        self.interest_rate = interest_rate
    def add_interest(self):
        total = self.balance * self.interest_rate
        self.balance += total 
        self.history.append(f'Interest +{total}')
        return self.balance
# Hau = SavingAccount('Hau', 0.6, 10)
# print(Hau.deposit(10))
# print(Hau.withdraw(30))
# print(Hau.add_interest())
# Hau.balance = -100
# print(Hau.show_balance())
# Hau.print_history()

from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @abstractmethod
    def final_price(self):
        pass
class RegularProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
    def final_price(self):
        return self.price
class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount
    def final_price(self):
        final = self.price - (self.price * (self.discount / 100))
        return final
class TaxedProduct(Product):
    def __init__(self, name, price, tax_percent):
        super().__init__(name, price)
        self.tax_percent = tax_percent
    def final_price(self):
        final = self.price + (self.price * (self.tax_percent / 100))
        return final
def print_receipt(products):
    total = 0
    for product in products:
        price = product.final_price()
        print(f'{product.name} : {price}')
        total += price
    return total
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, product):
        self.items.append(product)
    def remove_item(self, product_name):
        find =  False
        name = None
        for value in self.items:
            if value.name == product_name:
                name = value
                self.items.remove(name)
                find = True
                break
        if find == False:
            print('Not find product')
    def total(self):
        total = 0
        for pro in self.items:
            price = pro.final_price()
            total += price
        return total
    def checkout(self):
        for i in self.items:
            price = i.final_price()
            print(f'{i.name} : {price}')


# products = [
#        RegularProduct("Bút bi", 5000),
#        DiscountedProduct("Áo thun", 200000, 20),
#        TaxedProduct("Laptop", 15000000, 10),
#    ]
# print_receipt(products)
# cart = ShoppingCart()
# cart.add_item(RegularProduct("Bút bi", 5000))
# cart.add_item(DiscountedProduct("Áo thun", 200000, 20))
# cart.add_item(TaxedProduct("Laptop", 15000000, 10))

# cart.checkout()

# cart.remove_item("Bút bi")
# cart.checkout()   # kiểm tra bút bi đã bị xóa chưa

# cart.remove_item("Không tồn tại")

class Employee:
    company_name = "OOP"
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    @staticmethod
    def is_valid_salary(salary):
        if salary > 0:
            return True
        else:
            return False
    @classmethod
    def from_string(cls, data_string):
        name, salary =data_string.split("-")
        return cls(name, salary)
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
class Bonus:
    def calculate_bonus(self):
        return self.salary * 0.1
class SeniorManager(Manager, Bonus):
    pass
sm = SeniorManager("Long", 20000000, 5)
print(sm.calculate_bonus())    # phải chạy được dù Bonus không có __init__ riêng
print(Employee.is_valid_salary(-5))     # gọi static method qua tên class
emp = Employee.from_string("Nam-15000000")
print(emp.name, emp.salary) 