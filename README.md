# Discord Ses Botu Projesi

Bu proje şunları sağlar: 3 Tane farklı Discord botu 3 Farklı ses kanalına bağlanır, o ses kanallarına bir üye katıldığında bir müzik çalma işlevi tetiklenir, isteğe bağlı ytRolü değişkenine bir kayıtçı rolünün ID sini ekleyebilirsiniz, kayıtçı ses kanalına girdiğinde çalınan ses otomatik olarak durur.  

(BU WELCOME BOTU BETA SÜRÜMDEDİR SES ALGILAMA ÖZELLİĞİ ŞİMDİLİK YOKTUR)


## Kullanılan Dil(ler)

<picture>
  <source srcset="https://skillicons.dev/icons?i=py" media="(prefers-color-scheme: dark)">
  <img src="https://skillicons.dev/icons?i=py">
</picture>


## Özellikler

- **Birden Fazla Bot:** Aynı anda üç botu farklı ses kanallarına bağlar.
- **Otomatik Ses Çalma:** Belirtilen bir ses dosyasını ses kanalında oynatır.
- **Rol Tabanlı Müzik Kontrolü:** Belirli bir role sahip kullanıcı ses kanalına katıldığında müziği durdurur.
- **Otomatik Bağlanma:** Botlar belirtilen ses kanallarına otomatik olarak bağlanır ve kullanıcılar kanala girdikçe müzik çalmaya başlar.

## Gereksinimler

- `discord.py` kütüphanesi (V2.0)
- Python 3.8+
- Bir Discord uygulaması ve üç farklı bot token'ı
- Ses dosyası (örnek: `merhabaoyuncu.mp3`)

## Kurulum

1. **Kütüphanaleri yükleyiniz:**

    ```bash
    pip install discord.py
    ```

2. **Bot Token lerini Ayarlayın:**

   `main()` fonksiyonundaki `bot_tokens` bot token lerini ekleyiniz

3. **Ses Kanalı ID'lerini Ayarlayın:**

   Botların bağlanacağı ses kanallarının ID'lerini öğrenip `voice_channel_ids` listesine ekleyiniz

4. **Ses Dosyasını Ayarlayın:**

   `sesYolu` değişkenini kullanarak çalmak istediğiniz ses dosyasının tam dosya yolunu ayarlayın. Örnek olarak, `/home/container/merhabaoyuncu.mp3` verilmiştir

5. **Rol ID'sini Ayarlayın:**

   Müziği durduracak role ait ID'yi `ytRolü` değişkenine girinizz

## Kullanım

1. Projeyi çalıştırmak için terminalde aşağıdaki komutu kullanın:

    ```bash
    python bot.py
    ```

2. Botlar aktif hale gelir ve belirlenen ses kanallarına bağlanır.

3. Bir kullanıcı, belirlenen role sahip olduğu ses kanalına katıldığında bot müziği durdurur.

4. **Manuel Bağlanma:** Eğer bot ses kanalından çıkmışsa, `.gir` komutuyla tekrar bağlanabilir. (Sadece bulunduğun ses kanalına)

## Komutlar

- `.gir`: Botu ses kanalına tekrar bağlar. (SADECE BULUNUDUGUN SES KANALINA GİRER)

## Hata Ayıklama

- Eğer bot bağlanmazsa veya ses dosyasını çalamıyorsa, terminaldeki hata mesajlarını kontrol edin. İzin hatası veya dosya yolunun yanlış olması durumunda gerekli düzenlemeleri yapın.

## Lisans

MIT Lisansı tarafından korunuyor


## Discord Hesabım

![My Discord](https://lantern.rest/api/v1/users/794909914760871967?svg=1&theme=dark&borderRadius=2&hideActivity=1&hideStatus=0)
