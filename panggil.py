import bangunRuang as br
import bangunDatar as bd

print("-----BANGUN RUANG-----")
print(f"volume kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"volume balok adalah {br.balok(3,3,3)}")
print(f"volume prisma segitiga adalah {br.prisma(18,15,26)}")
print(f"volume tabung adalah {br.tabung(5,10)}")
print(f"volume kerucut adalah {br.kerucut(4,9)}")

print("-----BANGUN DATAR-----")
print(f"luas persegi adalah {bd.persegi(5)}")
print(f"luas persegi panjang adalah {bd.persegiPanjang(10,5)}")
print(f"luas segitiga adalah {bd.segitiga(8,10)}")
print(f"luas lingkaran adalah {bd.lingkaran(4)}")
print(f"luas jajarGanjar adalah {bd.jajarGanjar(4,7)}")

