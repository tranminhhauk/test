from math import sqrt
class PhuongTrinhBac2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def delta_(self):
        delta = self.b * self.b - (4*self.a*self.c)
        return delta

    def tinhNghiem(self, dta):
        dta = self.delta_()
        if dta < 0:
            print('->>Phuong trinh vo nghiem')
        elif dta > 0:
            x1 = (- self.b + sqrt(dta)) / (2 *self.a)
            x2 = (- self.b - sqrt(dta)) / (2 *self.a)
            print(f'nghiem x1 = {x1}, nghiem x2 = {x2}')
def nhap_phuong_trinh():
    a = float(input('Nhap he so a: '))
    b = float(input('Nhap he so b: '))
    c = float(input('Nhap he so c: '))
    pt1 = PhuongTrinhBac2(a, b, c)
    return pt1
def save_at_file(pt1):
    with open('pt.txt', 'w', encoding= 'utf-8') as file:
        file.write(str(pt1.a) + '\n')
        file.write(str(pt1.b) + '\n')
        file.write(str(pt1.c) + '\n')
        print('saved')
def main():
    pt1 = None
    while True:
        print('1. Nhap he so a b c')
        print('2. tinh nghiem')
        print('3. luu vao file')
        inp = int(input('Nhap lua chon: '))
        if inp == 1:
            pt1 = nhap_phuong_trinh()
            input()
        elif inp == 2:
            if pt1 is not None:
                delta = pt1.delta_()
                pt1.tinhNghiem(delta)
            input()
        elif inp == 3:
            save_at_file(pt1)

        else:
            break
main()