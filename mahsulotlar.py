# Telegram BOT uchun harakat
#yancharGAMING

#if-else shartlari va tarmoqlanish

mahsulotlar = ['pepsi', 'fanta', 'anor', 'olma', 'tarvuz', 'uzum', 'non', 'sovun', 'sut', 'qatiq']
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n + 1}-mahsulotni qo'shing\t"))
#for mahsulot in savat:
#    if mahsulot.lower() in mahsulotlar:
#        print(f"Do'konimizda {mahsulot} bor")
#    else: print(f"Do'konimizda {mahsulot} yo'q")

bor_mahsulotlar = []
yoq_mahsulotlar = []

for mahsulot in savat:
    if mahsulot.lower() in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else: yoq_mahsulotlar.append(mahsulot)

if not yoq_mahsulotlar: print("Siz so'ragan barcha mahsulotlar do'konimizda bor.")
else: print("Do'konimizda quyidagi mahsulotlar yo'q:")
for yoq_mahsulot in yoq_mahsulotlar:
    print(yoq_mahsulot)
    