# Praktikum 1 Metode Bolzano
## Kelas E Kelompok 2
Nama Kelompok :
- 5025211235 Ketut Arda Putra Mahotama Sadha
- 5025211009 Muhammad Rafif Tri Risqullah
- 5025211241 Angga Saputra

![Screenshot 2022-10-26 223449](https://user-images.githubusercontent.com/114855785/198070567-53fb0121-ab64-43e7-b1d7-b9e75f21461b.png)

Screenshot diatas adalah tampilan dari program metode bolzano. Program diatas menunjukkan plot dalam selang batasan bawah dan atas per iterasi, serta menunjukkan titik tengah berdasarkan batasan tersebut. Informasi tambahan yaitu selisih antara titik prediksi serta titik kenyataanya (ditunjukkan dengan garis oranye).

## Penjelasan Singkat Metode Bolzano
Metode Bolzano disebut pula sebagai metode Setengah Interval (Interval Halving), metode Bagi Dua, metode Biseksi, atau metode Pemotongan Biner. Secara singkat metode bolzano bekerja dengan menggunakan dua batasan yaitu batasan atas dan bawah. Titik nol fungsi terletak diantara kedua batasan tersebut. Titik tengah diantara kedua batasan tersebut akan selalu lebih dekat terhadap titik nol fungsi. Oleh karena itu, titik tengah akan dijadikan batasan atas atau bawah (Berdasarkan tanda dari f(xtengah) ) yang baru.

![image](https://user-images.githubusercontent.com/114855785/199007275-5ad3d777-5620-4859-ab25-c2e8421e7324.png)

#### Pseudocode
```
START
Batasan bawah = n   
Batasan atas = n+k 
// n = 0,1,2,...
// k = 0,1,2,...
// Titik nol f(x) berada diantara Batasan bawah dan atas
DO
  Titik tengah = (Batasan bawah + Batasan atas) / 2
  PRINT Titik tengah
  IF Tanda f(Batasan bawah) == Tanda f(Titik tengah)
    Batasan bawah = Titik tengah
  ELSE
    Batasan atas = Titik tengah
WHILE Kurang presisi // Berapa angka di belakang koma
END
```
