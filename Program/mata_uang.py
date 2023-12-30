def mu(mataUang, nilai):
     if mataUang == "KWD" or mataUang == "kwd":
          kwd = nilai
          idr = kwd * 50.100
          bhd = kwd * 1.227
          omr = kwd *1.252
          jod = kwd * 2.307
          gbp = kwd * 2.56
          gip = kwd * 2.56
          kyd = kwd * 2.67
          chf = kwd * 2.74
          eur = kwd * 2.95
          print(f"""
          kwd = {kwd},
          idr = {idr},
          bhd = {bhd},
          omr = {omr},
          jod = {jod},
          gbp = {gbp},
          gip = {gip},
          kyd = {kyd},
          chf = {chf},
          eur = {eur},
""")
     elif mataUang == "omr" or mataUang == "omr":
          omr = nilai
          idr = omr * 40.018
          bhd = omr * 0.980
          kwd = omr * 0.799
          jod = omr * 1.843
          gbp = omr * 2.04
          gip = omr * 2.04
          kyd = omr * 2.13
          chf = omr * 2.19
          eur = omr * 2.35
          print(f"""
          kwd = {kwd},
          idr = {idr},
          bhd = {bhd},
          omr = {omr},
          jod = {jod},
          gbp = {gbp},
          gip = {gip},
          kyd = {kyd},
          chf = {chf},
          eur = {eur},
""")
     elif mataUang == "bhd" or mataUang == "bhd":
          bhd = nilai
          idr = bhd * 40.843
          kwd = bhd * 0.815
          omr = bhd / 0.980
          jod = bhd * 1.881
          gbp = bhd * 2.08
          gip = bhd * 2.08
          kyd = bhd * 2.18
          chf = bhd * 2.23
          eur = bhd * 2.40
          print(f"""
          kwd = {kwd},
          idr = {idr},
          bhd = {bhd},
          omr = {omr},
          jod = {jod},
          gbp = {gbp},
          gip = {gip},
          kyd = {kyd},
          chf = {chf},
          eur = {eur},
""")
     elif mataUang == "jod" or mataUang == "jod":
          jod = nilai
          idr = jod * 21.716
          bhd = jod * 0.532
          omr = jod * 0.543
          kwd = jod * 0.433
          gbp = jod *1.11
          gip = jod * 1.11
          kyd = jod * 1.16
          chf = jod * 1.19
          eur = jod * 1.28
          print(f"""
          kwd = {kwd},
          idr = {idr},
          bhd = {bhd},
          omr = {omr},
          jod = {jod},
          gbp = {gbp},
          gip = {gip},
          kyd = {kyd},
          chf = {chf},
          eur = {eur},
""")
     elif mataUang == "gbp" or mataUang == "gbp":
          gbp = nilai
          idr = gbp * 19.602
          bhd = gbp * 0.480
          omr = gbp * 0.490
          jod = gbp * 0.903
          kwd = gbp * 0.391
          gip = gbp * 1
          kyd = gbp * 1.04
          chf = gbp * 1.07
          eur = gbp * 1.15
          print(f"""
          kwd = {kwd},
          idr = {idr},
          bhd = {bhd},
          omr = {omr},
          jod = {jod},
          gbp = {gbp},
          gip = {gip},
          kyd = {kyd},
          chf = {chf},
          eur = {eur},
""")
     elif mataUang == "gip" or mataUang == "gip":
          gip = nilai
          idr = gip * 19.602
          bhd = gip * 0.480
          omr = gip * 0.490
          jod = gip * 0.903
          gbp = gip * 1
          kwd = gip * 0.391
          kyd = gip *1.04
          chf = gip * 1.07
          eur = gip * 1.15
          print(f"""
          kwd = {kwd},
          idr = {idr},
          bhd = {bhd},
          omr = {omr},
          jod = {jod},
          gbp = {gbp},
          gip = {gip},
          kyd = {kyd},
          chf = {chf},
          eur = {eur},
""")
     elif mataUang == "kyd" or mataUang == "kyd":
          kyd = nilai
          idr = kyd * 18.776
          bhd = kyd * 0.460
          omr = kyd * 0.469
          jod = kyd * 0.865
          gbp = kyd * 0.96
          gip = kyd * 0.96
          kwd = kyd * 0.375
          chf = kyd * 1.03
          eur = kyd * 1.10
          print(f"""
          kwd = {kwd},
          idr = {idr},
          bhd = {bhd},
          omr = {omr},
          jod = {jod},
          gbp = {gbp},
          gip = {gip},
          kyd = {kyd},
          chf = {chf},
          eur = {eur},
""")
     elif mataUang == "chf" or mataUang == "chf":
          chf = nilai
          idr = chf * 18.297
          bhd = chf * 0.448
          omr = chf * 0.457
          jod = chf * 0.843
          gbp = chf * 0.093
          gip = chf * 0.93
          kyd = chf * 0.97
          kwd = chf * 0.365
          eur = chf * 1.08
          print(f"""
          kwd = {kwd},
          idr = {idr},
          bhd = {bhd},
          omr = {omr},
          jod = {jod},
          gbp = {gbp},
          gip = {gip},
          kyd = {kyd},
          chf = {chf},
          eur = {eur},
""")
     elif mataUang == "eur" or mataUang == "eur":
          eur = nilai
          idr = eur * 16.993
          bhd = eur * 0.416
          omr = eur * 0.425
          jod = eur * 0.783
          gbp = eur * 0.87
          gip = eur * 0.87
          kyd = eur * 0.91
          chf = eur * 0.93
          kwd= eur * 0.339
          print(f"""
          kwd = {kwd},
          idr = {idr},
          bhd = {bhd},
          omr = {omr},
          jod = {jod},
          gbp = {gbp},
          gip = {gip},
          kyd = {kyd},
          chf = {chf},
          eur = {eur},
""")
     elif mataUang == "idr" or mataUang == "idr":
          idr = nilai
          kwd = idr * 50.100
          bhd = idr * 40.843
          omr = idr * 40.018
          jod = idr * 21.716
          gbp = idr * 19.602
          gip = idr * 19.602
          kyd = idr * 18.776
          chf = idr * 19.297
          eur = idr * 16.993
          print(f"""
          kwd = {kwd},
          idr = {idr},
          bhd = {bhd},
          omr = {omr},
          jod = {jod},
          gbp = {gbp},
          gip = {gip},
          kyd = {kyd},
          chf = {chf},
          eur = {eur},
""")

     