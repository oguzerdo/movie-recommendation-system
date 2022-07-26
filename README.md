# Movie Recommender

![Untitled](images/Untitled.png)

## Film Tavsiye Sistemi Geliştirin

Repoyu aşağıdaki adresten indirelim.

**Gerekli paketleri yükleyelim**

`python3 -r requirements.txt`

`python ata_preparation.py`

`streamlit run app.py`

**.env dosyası içerisinde gerekli API kodunu girelim.**

`export MOVIE_API='WRITEYOURAPIKEYHERE’`

**Uygulamayı streamlit ile çalıştıralım.**

`streamlit run app.py`

## Heroku ile Uygulamanızı Dış Dünyaya açın

Aşağıdaki adresten Herokuya kayıt olalım.

[https://heroku.com/](https://heroku.com/)

Yeni bir proje oluşturalım.

![Untitled](images/Untitled%201.png)

Projemize bir isim verelim ve lokasyon bilgisini seçerek **Create app** ile devam edelim.

![Untitled](images/Untitled%202.png)

### Install the Heroku CLI

Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line).

**Heroku CLI yükleyelim.**

- **Mac:**

`brew tap heroku/brew && brew install heroku`

- **Windows**

Kullanıcıları bağlantıdan ilgili exe dosyasını indirip kurulum yapabilir.

İlgili proje dizininde terminal açarak sırasıyla aşağıdaki işlemleri yapalım.

Terminal üzerinden Heroku CLI aktif hale getirme.

`heroku login`

![Untitled](images/Untitled%203.png)

![Untitled](images/Untitled%204.png)

### Heroku üzerinde yeni bir Git Reposu oluşturalım.

Proje dizinimize girerek aşağıdaki kodları çalıştıralım. 

<aside>
💡 Aşağıdaki `movie-recommender-miuul` sizin koyduğunuz proje adı olacak.

</aside>

```
$ cd my-project/
$ git init
$ heroku git:remote -a movie-recommender-miuul
```

### Uygulamayı Heroku Reposuna gönderelim.

```
git checkout -b main
git add .
git commit -am "herokuya miuuldan selamlar"
git push heroku main
```

Bu işlem dosya boyutları sebebiyle uzun sürmekte. 

500 MB’lık bir sınır var, bu boyutu aştığımızda hata alıyoruz.

![Untitled](images/Untitled%205.png)

# BINGO!

![Untitled](images/Untitled%206.png)