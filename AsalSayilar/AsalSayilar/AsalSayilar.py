sayi =int(input("sayi:"))
asalmi=True
if sayi==1:
    print("1 asal sayı değildir")
for i in range(2,sayi):
    if(sayi%i==0):
        asalmi=False
        break
if asalmi:
    print("Sayı asaldır")
else:
    print("Sayı asal değildir")
