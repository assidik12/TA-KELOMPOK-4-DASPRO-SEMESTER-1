import Program.suhu
import Program.b_p
import Program.mata_uang
import Program.operator as po
while True:
     print("""
===================================================
           PROGRAM KALKULATOR KONVERSI
             Silahkan Pilih Program  
===================================================
           
     1. Kalkulator Operasi Aritmatika
     2. Konversi
     """)

     selectedProgam = input("Pilih Program (1/2) : ")
     print("-----------------------------------------")
     #kakulator
     def kalkulator(value1, value2, fungsi):
          if fungsi == 1 :  
               hasil = value1+value2
               print(f"Hasil dari {value1} tambah {value2} adalah {hasil}")
          elif fungsi == 2 : 
               hasil = value1-value2
               print(f"Hasil dari {value1} kurang {value2} adalah {hasil}")
          elif fungsi == 3 : 
               hasil = value1*value2
               print(f"Hasil dari {value1} kali {value2} adalah {hasil}")
          elif fungsi == 4 : 
               hasil = value1/value2
               print(f"Hasil dari {value1} bagi {value2} adalah {hasil}")
          else:
               print("Pilihan Tidak Terdaftar!")
               
     #konversi
     def konversi(select):
          if select == "suhu" or select == "1":
               print("""
     1. Celcius
     2. Fahrenheit
     3. Reamur
     4. Kelvin 
                     """)
               temperatur = input("Pilih Temperatur : ")
               suhu = int(input("Masukkan Suhu : "))
               Program.suhu.mySuhu(temperatur, suhu)
          elif select == "jarak"or select == "2":
               panjang = input("Pilih jarak dalam (km/m/dam/m/dm/cm/mm) : ")
               value = int(input("Masukan jarak yang kamu inginkan : "))
               Program.b_p.pj(panjang, value)   
          elif select == "berat" or select == "3":
               berat = input("Pilih berat dalam (kg/hg/dag/g/dg/cg/mg) : ")
               value = int(input("Masukan berat yang kamu inginkan : "))
               Program.b_p.pb(berat,value)
          elif select == "mata uang" or select == "4":
               mataUang = input("Masukan nilai mata uang [USA/IDN/DINAR] : ")
               nilai = int(input("Masukan nilai uang : "))
               Program.mata_uang.mu(mataUang, nilai)

     if selectedProgam == "1":
          print("""
     1. Tambah
     2. Kurang
     3. Kali
     4. Bagi 
                """)
          fungsi =input("Pilih Operasi Bilangan(1/2/3/4) : ")
          print("-----------------------------------------")
          value1 = int(input("Masukan nomor pertama : "))
          value2 = int(input("Masukan nomor kedua   : "))
          po.operator(fungsi, value1, value2)
     elif selectedProgam  == "2":
          print("""
     1. Suhu
     2. Jarak
     3. Berat
     4. Mata uang
          """)
          select = input("Pilih konversi yang anda inginkan  : ")
          print("-----------------------------------------")
          konversi(select)

     stop = input("Mau Menghitung Lagi? (Ya/Tidak): ")
     if stop == "ya" or stop == "Ya" or stop == "YA" :
          continue
     else:
          print("Program Selesai!")
          break          
