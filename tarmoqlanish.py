# Telegram BOT uchun harakat
#yancharGAMING

#if-else shartlari va tarmoqlanish

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars: 
#    if car == 'gm':
#        print(car.upper())
#    else: print(car.title())
#    if car != 'gm':
#        print(car.title())
#    else: print(car.upper())

#ism = input("Ismingizni kiriting:\t")
#if ism.lower() == 'admin':
#    print("Xush kelibsiz, Admin")
#else: print('Xush kelibsiz ', ism.title())

#print('Ikkita son kiriting.')
#a = int(input('Birinchi son:\t'))
#b = int(input('Ikkinchi son:\t'))
#if a == b: print('Sonlar teng.')

son = int(input('Istalgan sonni kiriting:\t'))
if son < 0: #print("Manfiy son.")
    print("Musbat son kiriting.")
#elif son > 0: print("Musbat son.")
else: #print("0 manfiy ham, musat ham emas.")
    print(f"{son} ning ildizi {son ** (1/2)} ga teng")