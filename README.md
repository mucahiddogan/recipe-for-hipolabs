# recipe-for-hipolabs
Hipo yaz stajı görevi

Yemek severlerin rahatlıkla istediği yemek tarifine ulaşabilmesini sağlayan platform.
Web sitesi üzerinde yeni bir kullanıcı oluşturarak yemek tariflerini paylaşabilir, düzenleyebilir veya silebilirsiniz.

Uygulamaya http://mucahiddogan.pythonanywhere.com üzerinden ulaşabilirsiniz.

Kendi localinizde çalıştırıp düzenleme yapmak için:

```bash
git clone https://github.com/mucahiddogan/recipe-for-hipolabs.git
cd recipe-for-hipolabs
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Eksikler(Yapılacaklar):
- Delete metodunda medya gibi öğelerin silinmesi yapılacak
- Vote ve Like sistemi ayarlanacak
- Malzemeye göre arama eklenecek
- User profil edit kısmı eklenecek
- Pathler düzenlenecek
- Authenticate olmuş userların izinleri güncellenecek

Teşekkürler :dizzy: ^^