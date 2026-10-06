"""Küçük bir bitkiyle ilgilenerek Python temellerini keşfet."""


def water_plant(plant):
    plant["water"] = min(100, plant["water"] + 20)
    print(f"Bitkini suladın. Su seviyesi: {plant['water']}/100")


def give_sunlight(plant):
    plant["sunlight"] = min(100, plant["sunlight"] + 20)
    print(f"Bitkin güneş ışığı aldı. Işık seviyesi: {plant['sunlight']}/100")


def show_status(plant):
    print(f"\nGün: {plant['day']}")
    print(f"Su: {plant['water']}/100")
    print(f"Güneş ışığı: {plant['sunlight']}/100")
    print(f"Sağlık: {plant['health']}/100")

    if plant["water"] < 30:
        print("Bitkin susamış.")
    elif plant["water"] > 80:
        print("Bitkin biraz fazla sulanmış.")
    else:
        print("Bitkinin su seviyesi iyi.")

    if plant["sunlight"] < 30:
        print("Bitkinin güneş ışığına ihtiyacı var.")
    elif plant["sunlight"] > 80:
        print("Bitkin biraz gölgede dinlenmeli.")
    else:
        print("Bitkinin ışık seviyesi iyi.")


def next_day(plant):
    plant["day"] += 1
    plant["water"] = max(0, plant["water"] - 15)
    plant["sunlight"] = max(0, plant["sunlight"] - 15)
    print(f"\n{plant['day']}. güne geçtin. Su ve ışık 15 puan azaldı.")

    # Sağlığı, gün sonunda kalan su ve ışık seviyelerine göre değerlendir.
    if plant["water"] < 30 or plant["sunlight"] < 30:
        plant["health"] = max(0, plant["health"] - 10)
        print("Su veya ışık yetersiz. Bitkinin sağlığı azaldı.")
    elif plant["water"] > 80 or plant["sunlight"] > 80:
        plant["health"] = max(0, plant["health"] - 5)
        print("Su veya ışık fazla. Bitkinin sağlığı biraz azaldı.")
    else:
        plant["health"] = min(100, plant["health"] + 5)
        print("Su ve ışık dengeli. Bitkin sağlığını koruyor veya toparlanıyor.")

    print(f"Sağlık: {plant['health']}/100")
    if plant["health"] == 0:
        print("Bitkin çok zayıf. Dengeli bakımla onu yeniden toparlayabilirsin.")


def main():
    plant = {
        "water": 50,
        "sunlight": 50,
        "health": 100,
        "day": 1,
    }
    print("Tiny Greenhouse'a hoş geldin!")
    print("Bu oyun terminalde çalışır; menü numarasını yazıp Enter'a bas.")
    print("1: suyu +20, 2: ışığı +20 artırır (en fazla 100).")
    print("4: günü bitirir; su ve ışık 15 azalır, ardından sağlık hesaplanır.")
    print("Hedef: gün sonunda kalan su ve ışığı 30–80 arasında tut.")
    show_status(plant)

    while True:
        print("\n1. Bitkiyi sula")
        print("2. Güneş ışığı ver")
        print("3. Bitkinin durumunu kontrol et")
        print("4. Sonraki güne geç")
        print("5. Çıkış")
        choice = input("Seçimin: ").strip()

        if choice == "1":
            water_plant(plant)
        elif choice == "2":
            give_sunlight(plant)
        elif choice == "3":
            show_status(plant)
        elif choice == "4":
            next_day(plant)
        elif choice == "5":
            print("Serayı kapattın. Görüşmek üzere!")
            break
        else:
            print("Lütfen 1 ile 5 arasında bir seçim yap.")


if __name__ == "__main__":
    main()
