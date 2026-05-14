# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, saya membangun sistem machine learning untuk mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout dan faktor-faktor yang berkaitan dengan dropout, sehingga mahasiswa tersebut dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Permasalahan bisnis yang ingin diselesaikan antara lain:

1. Tingginya angka dropout di Universitas.
2. Sulit mengetahui faktor utama yang mempengaruhi dropout.
3. Belum ada sistem monitoring dropout secara singkat.
4. Universitas membutuhkan model prediksi untuk mendeteksi mahasiswa yang berpotensi dropout.

### Cakupan Proyek
Cakupan proyek yang dikerjakan meliputi:

1. Melakukan eksplorasi dan analisis data mahsiswa.
2. Membersihkan dan melakukan preprocessing data.
3. Melakukan visualisasi data untuk memahami pola dropout.
4. Membangun model machine learning menggunakan Random Forest.
5. Mengevaluasi performa model prediksi dropout.
6. Membuat business dashboard menggunakan Metabase.
7. Melakukan deployment model menggunakan Streamlit.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md

Setup environment:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Business Dashboard
Business dashboard dibuat menggunakan Metabase untuk membantu departemen HR memahami dan memonitor faktor-faktor yang mempengaruhi status dropout atau tidak.

Dashboard menampilkan beberapa insight utama seperti:
- Jumlah Mahasiswa berdasarkan status
- Pengaruh Nilai Semester 1 dan 2 terhadap status mahasiswa
- Pengaruh Mata Kuliah yang lulus semester 1 dan 2 terhadap status mahasiswa
- Pengaruh Evaluasi pada semester dua terhadap status mahasiswa

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Berdasarkan hasil eksplorasi data dan dashboard, ditemukan beberapa karakteristik yang berkaitan dengan tingkat status mahasiswa.

Mahasiswa yang memiliki nilai kecil pada semester 1 dan 2 lebih mudah dropout dibandingkan dengan mahasiswa yang memiliki nilai lebih besar. Rata-rata nilai semester 1 dan 2 yang mendapatkan dropout sebesar 6-8 dari 20. Selain itu, dropout juga banyak dipengaruhi oleh mata kuliah yang tidak lulus pada semester 1 dan 2. Rata-rata mahasiswa yang dropout hanya lulus sebanyak 2-3 mata kuliah saja.

Hasil visualisasi pada dashboard dan exploratory data analysis (EDA) menunjukkan bahwa pola dropout pada nilai akademik yang sangat rendah.

Model Random Forest yang dibangun berhasil mencapai performa yang cukup baik dengan accuracy sekitar 85%.

Business dashboard yang dibuat juga membantu Universitas memahami pola dropout secara visual sehingga dapat mendukung pengambilan keputusan yang lebih singkat dan efektif.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
