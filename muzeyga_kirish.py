# Telegram BOT uchun harakat
#yancharGAMING

#if-else shartlari va tarmoqlanish

yosh = int(input("Yoshingizni kiriting:\t"))
if yosh <= 4 or yosh >= 60:
    print("Kirish bepul.")
elif yosh < 18:
    print("Kirish narxi 10000 so'm.")
else: print("Kirish narxi 20000 so'm.")