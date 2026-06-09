# True or True    # True
# True or False   # True
# False or True   # True
# False or False  # False



# hari = input("Masukan hari : ").lower()

# if hari == "sabtu" or hari == "minggu" :
#     print ("Hari ini libur ")
# else: print("tidak libur")



# login = input("Username :  ").lower()
# password = input("password :  ")

# if login == ("admin" or "admin@123") and password =="123":
#     print ("Login berhasil")
# else : print("Login tidak berhasil")


total_belanja = int(input("Masukkan total belanja: "))
voucher = input("Punya voucher? (ya/tidak): ").lower()

if total_belanja >=200000 or voucher == "ya":
    print("anda mendapatkan voucher")
else : 
    print("anda tidak menadapatkan voucher")