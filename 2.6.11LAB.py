hour= int(input("starting time (hours):"))
mins= int(input("starting time (minutes):"))
dura= int(input("event duration (minutes:"))

toplam_dakika= mins+dura
ekstra_saat= toplam_dakika//60
son_dakika=toplam_dakika % 60
son_saat= (hour+ekstra_saat) %24

print (str(son_saat) + ":" + str(son_dakika))
