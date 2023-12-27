def mu(mataUang, nilai):
     if mataUang == "USD" or mataUang == "usd":
          usa = nilai
          idn = int(15430*nilai)
          dinar = int(nilai*3.25)
          print(f"indonesia dinar\tusa\n")
          print("-"*65)
          print(f"{idn}\t {dinar}\t {usa}")
     elif mataUang =="idr" or mataUang == "IDR":
          idn = nilai
          usa = nilai / 15430
          dinar = int(nilai / 50.211)
          print(f"indonesia dinar \t usa\n")
          print("-"*65)
          print(f"{idn}\t {dinar} \t {usa}")
     elif mataUang == "DINAR" or mataUang == "dinar":
          idn = int(nilai*50.211)
          usa = int(nilai*3.25)
          dinar = nilai
          print(f"indonesia dinar \t usa\n")
          print("-"*65)
          print(f"{idn}\t {dinar} \t {usa}")
     else:
          print("masukan mata uang yang telah di tentukan")