import Program.suhu
import Program.b_p
import Program.mata_uang
#program konversi temperatur
print("-------------------------------------------------")
print("\n    program konversi\n")
print("-------------------------------------------------")

select = input("""
pilih konversi [suhu/jarak/berat/mata uang] : 
""")

#program utama/rendering
if select == "suhu":
     temperatur = input("pilih temperatur [celcius/reamur/fahrenhait/kelvin] : ")
     suhu = int(input("masuksan suhu : "))
     Program.suhu.mySuhu(temperatur, suhu)
elif select == "jarak":
     panjang = input("pilih jarak dalm (km\hm/dam/m/dm/cm/mm)")
     value = int(input("masukan jarak yang kamuinginkan : "))
     Program.b_p.pj(panjang, value)   
elif select == "berat":
     berat = input("pilih jarak dalm (kg\hg/dag/g/dg/cg/mg)")
     value = int(input("masukan berat yang kamuinginkan : "))
     Program.b_p.pb(berat,value)
elif select == "mata uang":
     mataUang = input("masukan nilai mata uang [USA/IDN/DINAR] : ")
     nilai = int(input("masukan nilai uang : "))
     Program.mata_uang.mu(mataUang, nilai)
else:
     print("keyword not found")