# Python Learning Lab

Bu repository, Python'ın temel programlama kavramlarını küçük ve interaktif örneklerle göstermek amacıyla hazırlanmış iki projeden oluşmaktadır. Projeler ayrı klasörlerde, birbirinden bağımsız çalışır.

## Kurulum

Python 3.11 veya üzeri gerekir. Aşağıdaki komutları `python-learning-lab` klasöründe çalıştır. Windows'ta `python` yerine `py -3.11` kullanabilirsin.

Yalnızca Parcel Planet için:

```bash
python -m pip install -r parcel-planet/requirements.txt
```

## Parcel Planet

PyGame ile geliştirilmiş küçük bir kargo ayıklama oyunu. Paketin ağırlığını ve kırılganlığını değerlendirerek taşıma bandını seç: kırılgan paketler Hassas, kırılgan olmayan ve en az 10 kg olanlar Ağır, diğerleri Standart banda gider. Kırılganlık önceliklidir; 12 kg'lık kırılgan paket de Hassas banda gider. Doğru seçimde skor artar ve yeni paket gelir; yanlış seçimde aynı pakette tekrar deneyebilirsin.

Gösterdiği kavramlar:

- koşullar
- fonksiyonlar
- değişkenler ve listeler
- rastgele seçim ve kullanıcı etkileşimi

```bash
python parcel-planet/parcel_planet.py
```

## Tiny Greenhouse

Terminal üzerinden çalışan küçük bir dijital bitki uygulaması. Menü numarasını yazıp Enter'a bas: su ve ışık eylemleri ilgili değeri 20 artırır, sonraki güne geçince ikisi de 15 azalır. Gün sonunda kalan su ve ışığı 30–80 arasında tutarak bitkinin sağlığını koru. Harici kütüphane gerektirmez.

Gösterdiği kavramlar:

- döngüler
- koşullar
- fonksiyonlar ve kullanıcı girdisi
- sözlüklerle basit durum yönetimi

```bash
python tiny-greenhouse/tiny_greenhouse.py
```
