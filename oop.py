from math import sqrt
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def tinh_chu_vi(self):
        pass
    
    @abstractmethod
    def tinh_dien_tich(self):

        pass
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def tinh_chu_vi(self):
        print("Tinh chu vi tam giac")
    def tinh_dien_tich(self):
        print("Dien tich tam giac")


class Square(Shape):
    def __init__(self, a):
        self.a = a
    def tinh_chu_vi(self):
        print("Tinh chu vi SQUARe")
    def tinh_dien_tich(self):
        print("Tinh dien tich SQUARe")


class Circle(Shape):
    def __init__(self, a):
        self.a = a
    def tinh_chu_vi(self):
        print("Tinh chu vi Circle")
    def tinh_dien_tich(self):
        print("Tinh dien tich Circle")
    
# values = input("Nhap vao di: ")
# values = values.split(" ")
# obj = None
# if values[0] == "SQUARE":
#     obj = Square(values[1])
# elif values[0] == "TRIANGLE":
#     obj = Triangle(values[1], values[2], values[3])
# elif values[0] == "CIRCLE":
#     obj = Circle(values[1])
# else:
#     print("Invalid input")

# if obj != None:
#     obj.tinh_chu_vi()
#     obj.tinh_dien_tich()
#     print(type(obj))

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
    def save(self, file_name = 'hoa_don.txt'):
        total = 0
        with open(file_name, 'w', encoding= 'utf-8') as file:
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


import random
import string

class Book:
    def __init__(self, title, author, ip):
        self.title = title
        self.author = author
        self.ip = ip
        self.is_available = True
    def check_out(self):
        if self.is_available == False:
            print('error! this book is already check out')
            return False
        else:
            self.is_available = False
            return True
    def return_book(self):
        self.is_available = True
    def __str__(self):
        if self.is_available == True:
            status = 'ready'
        else:
            status = 'not ready'
        return f'{self.title} {self.ip} - {status}'
class Member:
    def __init__(self, name):
        self.name = name
        self.member_id = random.randint(1000, 9999)
        self.borrowed_book = []
        
    def borrow_book(self, book):
        if len(self.borrowed_book) >= 3:
            print('error! member is has more than 3 book')
            return False
        else:
            self.borrowed_book.append(book) 
            return True
       
    def return_book(self, book):
        if book in self.borrowed_book:
            self.borrowed_book.remove(book)
            return True
        else:
            print('error! book not in member list')
            return False
    def __str__(self):
        return f' {self.name} ID: {self.member_id} - Borrow {len(self.borrowed_book)}'

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        
    def add_book(self, book):
        self.books.append(book)
    def register_member(self, member):
        self.members.append(member)
    def check_out_book(self, member_name, ip):
        find_book = None
        for b in self.books:
            if b.ip == ip:
                find_book = b
                break
        find_member = None
        for mem in self.members:
            if mem.name == member_name:
                find_member = mem
                break
        if find_book and find_member:
            if find_book.check_out() == True:
                if find_member.borrow_book(find_book) == True:
                    return f'{member_name} muon thanh cong: {find_book.title}'
                else:
                    find_book.return_book()
                    return f'{member_name} da muon du 3 cuon'
            return f'{find_book.title} hien da duoc muon'
        return f' khong tim thay sach hoac thanh vien nay'
    def return_book(self, member_name, ip):
        find_book = None
        for b in self.books:
            if b.ip == ip:
                find_book = b
                break
        find_member = None 
        for m in self.members:
            if m.name == member_name:
                find_member = m
                break
        if find_book and find_member:
            if find_member.return_book(find_book) == True:
                find_book.return_book()
                return f'{member_name} da tra xong: {find_book.title}'
            return f'{find_book.title} khong co ttron {member_name}'
        return f'khong khop thong tin tra sach'
    
lib = Library('Thu vien')
with open('pt.txt', 'r', encoding= 'utf-8') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        values = line.split(',')

        if values[0] =='Book':
            obj = Book(values[1], values[2], values[3])
            lib.add_book(obj)
            print(f"da nap sach {obj.title} ")
        elif values[0] == 'Member':
            obj = Member(values[1])
            lib.register_member(obj)
            print(f'da tao thanh vien {obj.name}')
        elif values[0] == 'Borrow':
            ket_qua = lib.check_out_book(values[1], values[2])
            print(ket_qua)
        elif values[0] == 'Return':
            ket_qua = lib.return_book(values[1], values[2])
            print(ket_qua)


    