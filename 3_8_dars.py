# 3-dars mashg'ulotlari

#print("Hello world!")
#print(7*8-60)
#print("Salom dunyo")
#print('hayahay "Salom" hay haya')
#print("hayahay \"Salom\" hay haya")
#print("""Salom dunyo,
# Sen bunchalar gozalsan""")
#print("Bulbulman ohu-zor chekib, \ntoza gulzordan ayrildim")
#print("3 ning kvadrati", 3**2, "ga teng")

# 4-dars mashg'ulotlari

# ism="Behruz"
# yosh=19
# print(ism,yosh)
# print(yosh)
# holat = "men 👿 ma"
# familiya="Shoymurodov"
# print("mening ismim " + ism)
# print("Mening ismim " + familiya +" " + ism)
# ism_sharif=f"{ism} {familiya}"

# ism = input("Ismingiz nima? \n>>>")
# print("Mening ismim " + ism.title())

# 6-dars mashgulotlari
# a = 29
# temp = 36.6
# a, b, c = 10,3, 23
# Amaliy topshiriq
# Misol_1
# son = int(input("Istalgan sonni kiriting:"))
# print(son, " ning kvadrati:", son**2, " ga teng." )
# print(son, " ning kubi:", son**31, " ga teng." )

# Misol_2
# yosh = int(input("Yoshingiz nechida?\n>>>"))
# print("Siz ", 2024 - yosh, " yilda tug'ilgansiz.")

# Misol_3
# son1 = float(input("Birinchi sonni kiriting:"))
# son2 = float(input("Ikkinchi sonni kiriting:"))
# print("Sonlar yig'indisi:", son1 + son2, " ga teng.")
# print("Sonlar ayirmasi:", son1 - son2, " ga teng.")
# print("Sonlar kopaytmasi:", son1 * son2, " ga teng.")
# print("Sonlar bolinmasi:", son1 / son2, " ga teng.")

# 7 - dars mashgulotlari
# 1_topshiriq
# ismlar = ["Azizbek", "Zoirbek", "Quvonchbek"]
# print("Salom ", ismlar[0], " yaxshimisan oshna")
# print("Jigar ", ismlar[1], " ertaga neci para dars ekan")
# print("Oshnooo", ismlar[2], " ertaga kursga borasanmi?")

# 2_topshiriq
# sonlar = [12, 23, 67, -46, 45.6]
# print(sonlar[2] + sonlar[4])
# print(sonlar[0] - sonlar[3])
# sonlar[1] = -25
# sonlar[4] = sonlar[0]
# print(sonlar)

# 3_topshiriq
# t_shaxslar = ["al-Xorazmiy", "Amir Temur", "Alisher Navoiy", "Imom Buxoriy"]
# z_shaxslar = ["Elon Musk", "Muhammadali Eshonqulov", "Otajonim"]
# print("Iloji bolsa tarixiy shaxslardan ",  t_shaxslar.pop(1), " bilan \n", 
# "zamonaviy shaxslardan ", z_shaxslar.pop(2), " bilan suhbat qurardim")

# 4_topshiriq
# friends = []
# friends.append("Asror")
# friends.append("Abror")
# friends.append("Ahror")
# friends.append("Alyor")
# friends.append("Doniyor")
# friends.append("Asqar")
# friends.remove("Ahror")
# friends.remove("Asror")
# friends.append("Behruz")
# friends.insert(0, "Anvar")
# friends.insert(3, "Azim")
# mehmonlar = []
# mehmonlar.append(friends.pop(2))
# mehmonlar.append(friends.pop(-1))


# 8 - dars mashgulotlari

# cars = ['matiz', 'nexia', 'damas', 'Bmw', 'Audi', 'Mercedez Benz']
# cars.sort()
# print(cars)
# cars.sort(reverse = True)
# print(cars)

# cars = ['matiz', 'nexia', 'damas', 'Bmw', 'Audi', 'Mercedez Benz']
# print(sorted(cars))
# print(sorted(cars, reverse = True))

# sonlar = list(range(0,10))
# print(sonlar)
# toq_sonlar = list(range(1,10,2))
# print(toq_sonlar)

# oyliklar = [21000,36000,45000,4100,9400000,140000]
# max_oylik = max(oyliklar)
# print(max_oylik)

# min_oylik = min(oyliklar)
# print(min_oylik)

# all_oylik = sum(oyliklar)
# print(all_oylik)

# taomlar = ['gosht', 'tuxum', 'sasiska', 'banan', 'tvorog']
# nonushta = taomlar[:]

# qizlar = ("Sanoz", "Adisha", "Mohinur", "Malohat", "Zarina", "Zilola")
# qizlar = list(qizlar)
# qizlar = tuple(qizlar)


# 9 - dars mashgulotlari

# xonadoshlar = ['Muhammadqul', 'Quvonchbek', 'Abdurahim', 'Orolbek', 'Muhammadali']
# for suka in xonadoshlar:
#     print("Salomlar ", suka)
# print("Xayr ", suka)

# xonadoshlar = ['Muhammadqul', 'Quvonchbek', 'Abdurahim', 'Orolbek', 'Muhammadali']
# for xonadosh in xonadoshlar:
#     print(f"Hurmatli {xonadosh} ahvolingiz yaxshimi")

# numbers = list(range(1,11,2))
# for number in numbers:
#     print(f"{number} ning kvadrati {number**2} ga teng")

# sonlar = list(range(1,11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**3)
# print(sonlar)
# print(sonlar_kvadrati)    

# friends = []
# print("Who are your 5 best friends?")
# for n in range(5):
#     friends.append(input(f"{n+1}-dostingizni ismini kiriting:"))
# print(friends)

# 10 - dars mashgulotlari

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == "gm":
#        print(car.upper())
#     else:
#        print(car.title())

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != "gm":
#         print(car.title())
#     else:
#         print(car.upper())


# name = input("Login ismingizni kiriting\n>>>")
# if name == "admin":
#     print("Xush kelibsiz, Admin.Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print("Xush kelibsiz ", name)

# number1 = float(input("1 - sonni kiriting:"))
# number2 = float(input("2 - sonni kiriting:"))
# if number1 == number2:
#     print("Ikkala son teng ekan!")

# number = float(input("Enter the number:"))
# if number < 0:
#     print("Manfiy son")
# else:
#     print("Musbat son")

# son = float(input("Sonni kiriting:"))
# print(son**0.5) if son > 0 else print("Musbat son kiriting!")
    

# 11 - dars mashgulotlari
# son = int(input("Juft son kiriting:"))
# if son % 2 == 0:
#     print("Rahmat")
# else:
#     print(f"Juft son kiriting. {son} bu son juft emas")

# age = int(input("Yoshingiz nechida?\n>>>"))
# if age <= 4 or age >=60:
#     print("Kirish bepul")
# elif age <=18:
#     print("Narx 10000 som")
# else:
#     print("Narx 20000 som")

# mahsulotlar = ["olma", "anor", "uzum", "nok", "behi", "zardoli", "gilos", "dovcha", "olxori", "banan"]
# savat = []
# for n in range(1,6):
#     savat.append(input(f"Savatga {n} - mahsulotni kiriting:"))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Dokonimizda {mahsulot} bor")
#     else:
#         print(f'Dokonimizda {mahsulot} yoq')


# mahsulotlar = ["olma", "anor", "uzum", "nok", "behi", "zardoli", "gilos", "dovcha", "olxori", "banan"]
# savat = []
# for n in range(1,6):
#     savat.append(input(f"Savatga {n} - mahsulotni kiriting:"))


    
    






















