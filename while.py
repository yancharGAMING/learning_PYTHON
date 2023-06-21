# Telegram BOT uchun harakat
#yancharGAMING

#while tsikli loop

#kitoblar = []
#kitob = ' '
#while kitob.lower() != 'stop':
#    kitob = input("sevimli kitobingizni kiriting: (daturni to'xtatish uchun 'stop' so'zini kiriting)\t")
#    kitoblar.append(kitob)
#print('Dastur tugadi.')

#narx = {
 #       'a' : 2000,
  #      'b' : 3000,
   #     'c' : 10000}
#chiqish = ['stop', 'quit', 'exit']
#while True:
#    qiymat = input(f"Yoshingizni kiriting: (dasturni toxtatish uchun exit,stop yoki quit so'zini kiriting)\t")
#    if qiymat.lower() in chiqish:
#        break
#    yosh = int(qiymat)
#    if yosh < 7:
#        print(f"Kirish narxi {narx['a']} so'm.")
#    elif yosh < 18:
#        print(f"Kirish narxi {narx['b']} so'm.")
#    elif yosh < 60:
#        print(f"Kirish narxi {narx['c']} so'm.")
#    else: print('Kirish tekin.')
 
buyurtmalar = []
print("Buyurtmalaringizni kiriting:")
n = 1
while True:
    buyurtma = input(f"{n}-buyurtmani kiriting:\t").lower()
    buyurtmalar.append(buyurtma)
    chiqish = input('Yana buyurtmangiz bormi? (ha/yo\'q)\t')
    n += 1
    if chiqish.lower() != 'ha':
        break

e_bozor = {}
n = 1
while True:
    mahsulot = input(f"{n}-mahsulot nomini kiriting:\t").lower()
    narx = input(f"{mahsulot.title()}ning narxini kiriting:\t")
    e_bozor[mahsulot.lower()] = int(narx)
    chiqish = input("Yana mahsulot joylaysizmi? ha/yo\'q\t")
    n += 1
    if chiqish.lower() != 'ha':
         break
narx = 0
for buyurtma in buyurtmalar:
    if buyurtma in e_bozor.keys():
        print(f"{buyurtma.title()}ning narxi {e_bozor[buyurtma]} so'm.")
        narx += e_bozor[buyurtma]
    else:  print(f"Bizda {buyurtma} yo'q.")
print('Buyurtmangiz jami narxi', narx, 'so\'m bo\'ldi.')    
        
        
        