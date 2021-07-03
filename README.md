# spotify-playlist-turnusolu

## Ne işe yarıyor
Elinizdeki bir Spotify playlist'inde programda bulunan black_list adlı array içine yazılmış sanatçıların içeriği olup olmadığı aranıyor, eğer birine bile rastlarsa program "Bu playlist dinlenmez" diyip kendini kapatıyor. Yazılan sanatçıların herhangi biri yoksa herhangi bir sonuç vermeden kapanıyor.

## Kurulum öncesi gerekli araçlar
* Git
* Python 3.x

## Kurulum
Terminalde şu adımları takip ederek kurulum yapabilirsiniz:<br>
* git clone https://github.com/kayrakpinar/spotify-playlist-turnusolu.git<br>
* cd spotify-playlist-turnusolu<br>
* pip install requirements.txt<br>
veya <br>
python -m pip install requirements.txt

## Yapılandırma
Öncelikle Spotify'dan bir uygulama oluşturup uygulamanın ID ve Secret key'ini config.json dosyasında "YOUR SPOTIFY APP CLIENT ID" ve "YOUR SPOTIFY APP CLIENT SECRET KEY" değerleri yerine (Çift tırnakları silmeden) eklememiz gerekiyor. Şu bağlantıdan Spotify uygulaması oluşturma konusunda yardım alabilirsiniz: https://developer.spotify.com/documentation/general/guides/app-settings/<br>

Daha sonra spoList.py dosyasını herhangi bir IDE veya text editor ile açarak black_list adlı array içine dinlemek istemediğiniz artist isimlerini yazıyorsunuz.

## Kullanımı
Terminalde `python spoList.py` yazarak programımızı çalıştırdığında programa önce playlist URL adresi, daha sonra da playlist'in sahibi olan kullanıcı URL adresi verilmelidir. Devamında program kendi üstüne düşeni yapıp **Ne işe yarıyor** başlığında bahsedilen sonuçlardan birini verip kapanacaktır.
