import datetime
bugun = datetime.date.today()
yil = bugun.year
bayram_sana = datetime.date(2025,9,1)

if bugun >= bayram_sana:
    bayram_sana = datetime.date(2025 + 1,9,1)
qolgan_kunlar = (bayram_sana - bugun).days
print(f"Keyingi Mustaqillik bayrami sanasi ({bayram_sana})gacha {qolgan_kunlar} kun qoldi.")
