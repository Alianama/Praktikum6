def tampilkan(nama):
    print("Hello", nama, ".Selamat datang")


nama = "ari"
tampilkan(nama)
nama = "udin"
tampilkan(nama)

def hitung(a,b):
    return a + b
    
hitung(10, 20)
a = 10
b = 20
hitung(a, b)
print(hitung(a, b))

def tampilkan(nama, msg=" apa kabar?"):
    print("hello", nama,msg)

nama = "ali"
tampilkan(nama)

def tampilkan(*names):
    for nama in names:
        print("hello", nama, "Apa Kabar?")

tampilkan("ali", "dina", "udin")

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)
new_list = list(map(lambda x: x * 2 , my_list)) 
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)