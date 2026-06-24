class MonHoc:
    def __init__(self, maMh, tenMh, tc):
        self.maMh = maMh
        self.tenMh = tenMh
        self.tc = tc
    def hienThi(self):
        print('Ma mo hoc:', self.maMh)
        print('Ten mo hoc:', self.tenMh)
        print('So tin chi:', self.tc)
danh_sach = []
def nhapMH():
    mh_moi = int(input('Nhap so luong Mon Hoc moi: '))
    for i in range(mh_moi):
        maMh = input('Ma mon hoc: ')
        tenMh = input('Ten mon hoc: ')
        tc= input('So tin chi: ')
        mh = MonHoc(maMh, tenMh, tc)
        danh_sach.append(mh)
def hienThiDs():
    for i in range(len(danh_sach)):
        print("Thong tin mon hoc:", i + 1)
        danh_sach[i].hienthi()
def xoaMH(ma):
    # ma = input('Nhap ma mon hoc can xoa: ')
    for i in danh_sach:
        if i.maMh == ma:
            danh_sach.remove(i)
            break
def ghids():
    with open('monHoc.txt', 'w', encoding= 'utf-8') as file:
        n = len(danh_sach)
        for i in range(n):
            file.write(danh_sach[i].maMh + '\n')
            file.write(danh_sach[i].tenMh+ '\n')
            file.write(danh_sach[i].tc + '\n')
def doc():
    with open('monHoc.txt', 'r', encoding= 'utf-8') as file:
        return file.read()
def main():
    doc()
    while True:
        hienThiDs()
        inp = input ('1.Nhap Mon Hoc Moi: \n2.Xoa mon hoc:\n3.Xem ds mon hoc: \nNhap lua chon: ')
        if inp == '1':
            nhapMH()
            ghids()
        elif inp == '2':
            ma = input('Nhap ma mon hoc can xoa: ')
            xoaMH(ma)
            ghids()
            print(f'Mon Hoc da xoa')
        elif inp == '3':
            hienThiDs()
        else:
            break

