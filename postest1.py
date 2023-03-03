import random #Berfungsi untuk memasukan modul random pada code

def quickSort(arr): # function def untuk quick sort
    if len(arr) <= 1: # Jika panjang list yang ada pada list kurang dari atau sama dengan satu
        return arr # maka akan mengembalikan function
    else:
        pivot = arr[0] #pivot yang digunakan adalah elemen di list arr pada index ke-0
        print(f"Pivot : {pivot}") 
        less = [x for x in arr[1:] if x <= pivot] #jika nilai x kurang dari atau sama dengan pivot yang digunakan maka akan dimasukan pada variabel "less"
        greater = [x for x in arr[1:] if x > pivot]#jika nilai x lebih dari pivot yang digunakan maka akan dimasukan pada variabel "greater"
        return quickSort(less) + [pivot] + quickSort(greater) #mengembalikan nilai dari quicksort pada variabel "less" ditambah dengan nilai pivot dan ditambah quicksort pada variabel "greater"

def shellSort(data): # untuk menjalankan algoritma shell sort
    gap = (len(data)//2) #variabel "gap" menyimpan nilai panjang list atau data dibagi dengan dua
    b=0 #variabel "b" digunakan menyimpan nilai 0

    while gap > 0 : #selama nilai variabel "gap" lebih dari 0 maka akan menjalankan function didalamnya
        for o in range(gap,len(data)):#melakukan perulangan dengan jarak antara nilai variabel "gap" sampai dengan nilai panjang list "data"
            value = data[o] #variabel value digunakan untuk menyimpan list "data" pada index ke-i
            k = o #nilai variabel "k" sama dengan "o" 

            while k >= gap and data[k-gap] > value: #selama nilai variabel "j" lebih dari atau sama dengan nilai variabel "gap" dan elemen list data index ke-"j" dikurangi "gap"
                data[k] = data[k-gap] #elemen list "data" index ke-"j" sama dengan elemen "data" index ke-"j" dikurangi dengan "gap"
                j-=gap #nilai variabel "j" dikurangi nilai variabel "gap"

            data[k] = value #elemen "data" index ke-"j" sama dengan nilai variabel "value"
            print(data)
        print("Iterasi ke",b,": ",data,"dengan gap ",gap )
        b+=1 #nilai variabel "b" ditambah dengan satu

        gap //= 2 #setelah setiap iterasi maka nilai variabel "gap" akan dibagi dua

    return data #mengembalikan nilai dari variabel "data" setelah function shell sort selesai

angka = [0,1,3,5,6,7,10,18,21,45] #menyimpan list yang berisi angka
random.shuffle(angka) #berguna untul mengacak data dari variabel "angka" 
while True: #digunakan untuk melakukan perulangan
    print("""
====================      
|1. Untuk Quicksort|
|2. Untuk Shellsort|
====================
""")
    a = input("Masukan Sorting Yang Ingin Digunakan: ") #digunakan untuk menyimpan inputan sorting yang akan digunakan
    if a == "1": #jika memilih "1" maka akan menjalankan function quick sort
        print(f"list sebelum disort: {angka}")
        print(f"list setelah disort: {quickSort(angka)}")
        break #berfungsi sebagai memberhentikan perulangan ketika program sudah selesai dijalankan
    elif a == "2": #jika memilih "2" maka akan menjalankan functionon shell sort
        print(f"list sebelum disort: {angka}")
        print(f"list setelah disort: {shellSort(angka)}")
        break
    else:
        print("Input salah atau tidak ada") #jika inputan yang dimasukan salah maka akan mengulangi inputan