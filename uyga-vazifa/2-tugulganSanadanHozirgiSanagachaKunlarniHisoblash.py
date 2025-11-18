import datetime
try:
    tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))
    tugilgan_oy = int(input("Tug'ilgan oyingizni kiriting: "))
    tugilgan_kun = int(input("Tug'ilgan kuningizni kiriting: "))

    tugilgan_sana = datetime.date(tugilgan_yil, tugilgan_oy, tugilgan_kun )
    bugungi_sana = datetime.datetime.now().date()

    farq = bugungi_sana - tugilgan_sana
    otgan_kunlar = farq.days

    print("_" * 30)
    print(f"Sizning tug'ilgan sanangiz: {tugilgan_sana}")
    print(f"Bugungi sana: {bugungi_sana}")
    print(f"Tug'ilgan kundan buyon {otgan_kunlar} kun o'tdi.")
except ValueError:
    print("\n Xatolik: Iltimos, yil, oy va kunni butun son (raqam) shaklida kiriting ")
except Exception as e:
    print(f"\n xatolik yuz berdi: sanani noto'g'ri kiritdingiz! {e}")
    