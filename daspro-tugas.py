#program konversi temperatur
print("-------------------------------------------------")
print("\n    program konversi\n")
print("-------------------------------------------------")

select = input("""
pilih konversi [suhu/jarak/berat/mata uang] : 
""")

#suhu
if select == "suhu":
    temperatur = input("pilih temperatur [celcius/reamur/fahrenhait/kelvin] : ")
    suhu = int(input("masuksan suhu : "))
    #konversi from celcius
    if temperatur == "celcius":
        reamur = (4/5) * suhu
        print(f"suhu konversi = {reamur} reamur")
        fahrenhait = ((9/5) * suhu) + 32
        print(f"suhu konversi = {fahrenhait} fahrenhait")
        kelvin = suhu + 273.15
        print(f"suhu konversi = {kelvin} kelvin")
    # konversi from reamur
    elif temperatur == "reamur":
        celcius = (5/4) * suhu
        print(f"suhu konversi = {celcius} celcius")
        fahrenhait = (9/4) * suhu + 32
        print(f"suhu konversi = {fahrenhait} fahrenhait")
        kelvin = (5/4) * suhu + 273
        print(f"suhu konversi = {kelvin} kelvin")
    # konversi from fahrenhait
    elif temperatur == "fahrenhait":
        celcius = 5/9 * (suhu-32)
        print(f"suhu konversi = {celcius} celcius")
        reamur = 4/9 * (suhu-32)
        print(f"suhu konversi = {reamur} reamur")
        kelvin = 5/9 * (suhu-32) + 273
        print(f"suhu konversi = {kelvin} kelvin")
    # konversi from kelvin
    elif temperatur == "kelvin":
            celcius =suhu - 273
            print(f"suhu konversi = {celcius} celcius")
            reamur = 4/5 * (suhu - 273)
            print(f"suhu konversi = {reamur} reamur")
            kelvin = 9/5 * (suhu-273) + 32
            print(f"suhu konversi = {kelvin} kelvin")
    else:
         print("masukan value dengan benar!")

elif select == "jarak":
     panjang = input("pilih jarak dalm (km\hm/dam/m/dm/cm/mm)")
     value = int(input("masukan jarak yang kamuinginkan : "))
     if panjang == "km":
          km = value
          hm = value * 10
          dam = value * 100
          m = value * 1000
          dm = value * 10000
          cm = value * 100000
          mm = value * 1000000
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "hm":
          km = value / 10
          hm = value
          dam = value * 10
          m = value * 100
          dm = value * 1000
          cm = value * 10000
          mm = value * 100000
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "dam":
          km = value / 100
          hm = value / 10
          dam = value
          m = value * 10
          dm = value * 100
          cm = value * 1000
          mm = value * 10000
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "m":
          km = value / 1000
          hm = value / 100
          dam = value / 10
          m = value 
          dm = value * 10
          cm = value * 100
          mm = value * 1000
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "dm":
          km = value / 10000
          hm = value / 1000
          dam = value / 100
          m = value / 10
          dm = value 
          cm = value * 10
          mm = value * 100
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "cm":
          km = value / 100000
          hm = value / 10000
          dam = value / 1000
          m = value / 100
          dm = value /10
          cm = value 
          mm = value * 10
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "mm":
          km = value / 1000000
          hm = value / 100000
          dam = value / 10000
          m = value / 1000
          dm = value /100
          cm = value / 10
          mm = value
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     else:
        print("masukan dengan benar!")

elif select == "berat":
     berat = input("pilih jarak dalm (kg\hg/dag/g/dg/cg/mg)")
     value = int(input("masukan berat yang kamuinginkan : "))
     if berat == "kg":
          kg = value
          hg = value * 10
          dag = value * 100
          g = value * 1000
          dg = value * 10000
          cg = value * 100000
          mg = value * 1000000
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
     elif berat == "hg":
          kg = value / 10
          hg = value
          dag = value * 10
          g = value * 100
          dg = value * 1000
          cg = value * 10000
          mg = value * 100000
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
     elif berat == "dag":
          kg = value / 100
          hg = value / 10
          dag = value
          g = value * 10
          dg = value * 100
          cg = value * 1000
          mg = value * 10000
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
     elif berat == "g":
          kg = value / 1000
          hg = value / 100
          dag = value / 10
          g = value 
          dg = value * 10
          cg = value * 100
          mg = value * 1000
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
     elif berat == "dg":
          kg = value / 10000
          hg = value / 1000
          dag = value / 100
          g = value / 10
          dg = value 
          cg = value * 10
          mg = value * 100
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
     elif berat == "cg":
          kg = value / 100000
          hg = value / 10000
          dag = value / 1000
          g = value / 100
          dg = value /10
          cg = value 
          mg = value * 10
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
     elif berat == "mg":
          kg = value / 1000000
          hg = value / 100000
          dag = value / 10000
          g = value / 1000
          dg = value /100
          cg = value / 10
          mg = value
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
     else:
        print("masukan dengan benar!")

elif select == "mata uang":
     mataUang = input("masukan nilai mata uang [USA/IDN/DINAR] : ")
     nilai = int(input("masukan nilai uang : "))
     if mataUang == "USA" or mataUang == "usa":
          usa = nilai
          idn = 16000*nilai
          dinar = 16000*nilai
          print(f"indonesia dinar \t usa\n")
          print("-"*65)
          print(f"{idn}\t {dinar} \t {usa}")
     elif mataUang =="idn" or mataUang == "IDN":
          idn = nilai
          usa = nilai / 16000
          dinar = nilai / 5000
          print(f"indonesia dinar \t usa\n")
          print("-"*65)
          print(f"{idn}\t {dinar} \t {usa}")
     elif mataUang == "DINAR" or mataUang == "dinar":
          idn = nilai*3500
          usa = nilai*13000
          dinar = nilai
          print(f"indonesia dinar \t usa\n")
          print("-"*65)
          print(f"{idn}\t {dinar} \t {usa}")
     else:
          print("masukan mata uang yang telah di tentukan")