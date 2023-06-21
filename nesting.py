# Telegram BOT uchun harakat
#yancharGAMING

#zohid = {'name' : 'Zohid',
#         'age' : 25,
#         'year' : 1998,
#         'job' : 'student',
#         'from' : 'qashqadaryo',
#        'live' : 'tashkent'}
#sanjar = {'name' : 'Sanjar',
#         'age' : 25,
#         'year' : 1998,
#         'job' : 'cooker',
#         'from' : 'jizzax',
#        'live' : 'london'}
#olim = {'name' : 'olim',
#         'age' : 25,
#         'year' : 1998,
#         'job' : 'student',
#         'from' : 'surxondaryo',
#        'live' : 'scotland'}
#bek = {'name' : 'bekmurod',
#         'age' : 23,
#         'year' : 2000,
#         'job' : 'student',
#         'from' : 'qashqadaryo',
#        'live' : 'tashkent'}
#friends = [zohid, sanjar, olim, bek]
#orders = {1:'1st', 2:'2nd', 3:'3rd'}
#for boy in friends:
#    print(f"{boy['name'].title()} was born in {boy['year']} in {boy['from'].title()}. "
#          f"He is {boy['age']} years old and living in {boy['live'].title()}. "
#          f"He is a {boy['job']} right now.")
#for boy in friends:
#     boy['phones'] = []
#     n = int(input(f"How many phones has {boy['name'].title()}?\t"))
#     for k in range(n):
#         if k + 1 in orders:
#             phone = input(f"What is {boy['name'].title()}'s {orders[k+1]} phone?\t")
#         else: 
#             phone = input(f"What is {boy['name'].title()}'s {k + 1}th phone?\t")
#         boy['phones'].append(phone)
#for boy in friends:
#    print(f"{boy['name'].title()}'s phones are:")
#    for phone in boy['phones']:
#        print(phone.title(), end = ' ')
#    print("")

kinolar = {
    'ali' : ['terminator', 'rambo', 'titanic'],
    'vali' : ['tenet', 'inception', 'interstellar'],
    'hasan' : ['abdullajon', 'bomba', 'shaytanat'],
    'husan' : ['mahallada duv-duv gap', 'john wick']
    }
for ism,kino in kinolar:
    print(ism.title(), "ning sevimli kinolai:")
    for kinno in kino:
        print(kinno.title())
        

