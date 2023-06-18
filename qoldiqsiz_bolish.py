# Telegram BOT uchun harakat
#yancharGAMING

#if-else shartlari va tarmoqlanish

son = int(input('Istalgan butun son kiriting:\t'))

for a in range(2,11):
    if son % a == 0:
        print(f"{son} soni {a} ga qoldiqsiz bo'linadi")