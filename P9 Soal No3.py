def nilai(n=0):
    if n <= 60:
        print(f"nilai {n} Tidak Lulus")
    elif n > 60 and n <= 100:
        print(f"nilai {n} Lulus")
    else:
        print(f"nilai {n} Tidak Diketahui")
nilai(80)
nilai(60)