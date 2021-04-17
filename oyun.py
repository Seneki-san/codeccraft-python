import random
seçenek=["taş","kağıt","makas"]
taş=seçenek[0]
kağıt=seçenek[1]
makas=seçenek[2]
print("taş kağıt makasa hoş geldin \nbakalım beni yenebilecek misin ?\n çıkış yazarak çıkabilirsin")
while True:
    seç=input("seçenek gir: ")
    bilgiseç=random.choice(seçenek)
    if seç == taş:
        if bilgiseç == taş:
            print("senin seçimin",seç)
            print("bilgisayarın seçimi",bilgiseç)
            print("berabere")
        elif bilgiseç == makas:
            print("senin seçimin",seç)
            print("bilgisayarın seçimi",bilgiseç)
            print("kazandın")
        else:
            print("senin seçimin",seç)
            print("bilgisayarın seçimi",bilgiseç)
            print("kaybettin")
    elif seç == "çıkış":
        print("iyi mücadele ettin")
        break
    else:
        print("lütfen üç seçenekten birini giriniz")
    if seç == kağıt:
        if bilgiseç == taş:
            print("senin seçimin",seç)
            print("bilgisayarın seçimi",bilgiseç)
            print("kazandın")
        elif bilgiseç == makas:
            print("senin seçimin",seç)
            print("bilgisayarın seçimi",bilgiseç)
            print("kaybettin")
        else:
            print("senin seçimin",seç)
            print("bilgisayarın seçimi",bilgiseç)
            print("berabere")
    if seç == makas:
        if bilgiseç == taş:
            print("senin seçimin",seç)
            print("bilgisayarın seçimi",bilgiseç)
            print("kaybettin")
        elif bilgiseç == makas:
            print("senin seçimin",seç)
            print("bilgisayarın seçimi",bilgiseç)
            print("berabere")
        else:
            print("senin seçimin",seç)
            print("bilgisayarın seçimi",bilgiseç)
            print("kazandın")