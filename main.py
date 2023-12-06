import Program.suhu
import Program.b_p
import Program.mata_uang

print("""
     PROGRAM KALKULATOR DAN KONVERSI
          silahkan pilih fungsi
      1. kalkulator
      2. konversi
""")

selectedProgam = input("pilih program (1/2) : ")


#kakulator
def kalkulator(value1, value2, fungsi):
     if fungsi == "tambah":
          hasil = value1+value2
     elif fungsi == "kurang":
          hasil = value1-value2
     elif fungsi == "kali":
          hasil = value1*value2
     elif fungsi == "bagi":
          hasil = value1/value2
     print(f"hasil dari {value1} {fungsi} {value2} adalah {hasil}")


#konversi
def konversi(select):
     if select == "suhu" or select == "1":
          print(" celcius \n fahrenhait \n reamur \n kelvin ")
          temperatur = input("pilih temperatur : ")
          suhu = int(input("masukan suhu : "))
          Program.suhu.mySuhu(temperatur, suhu)
     elif select == "jarak"or select == "2":
          panjang = input("pilih jarak dalm (kmh/m/dam/m/dm/cm/mm)")
          value = int(input("masukan jarak yang kamuinginkan : "))
          Program.b_p.pj(panjang, value)   
     elif select == "berat" or select == "3":
          berat = input("pilih jarak dalm (kg/hg/dag/g/dg/cg/mg)")
          value = int(input("masukan berat yang kamuinginkan : "))
          Program.b_p.pb(berat,value)
     elif select == "mata uang" or select == "4":
          mataUang = input("masukan nilai mata uang [USA/IDN/DINAR] : ")
          nilai = int(input("masukan nilai uang : "))
          Program.mata_uang.mu(mataUang, nilai)

if selectedProgam == "1":
     print(" tambah \n kurang \n kali \n bagi ")
     fungsi = input("pilih kalkulator ")
     value1 = int(input("masukan nomor kesatu : "))
     value2 = int(input("masukan nomor kedua : "))
     kalkulator(value1, value2, fungsi)
elif selectedProgam  == "2":
     print("""
     1. suhu
     2. jarak
     3. berat
     4. mata uang
     """)
     select = input("pilih konversi yang anda inginkan  : ")
     konversi(select)




