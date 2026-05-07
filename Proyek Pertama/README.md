# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang memiliki lebih dari 1000 karyawan yang tersebar di berbagai wilayah. Tingginya tingkat attrition karyawan menjadi salah satu tantangan utama bagi departemen HR karena dapat mempengaruhi produktivitas perusahaan, biaya rekrutmen, serta stabilitas organisasi.

Melalui proyek ini dilakukan analisis data dan pembangunan model machine learning untuk memahami faktor-faktor yang berkaitan dengan attrition serta membantu perusahaan memprediksi potensi resign karyawan.

### Permasalahan Bisnis

Permasalahan bisnis yang ingin diselesaikan pada proyek ini antara lain:

1. Tingginya tingkat attrition karyawan dalam perusahaan.
2. Sulitnya mengidentifikasi faktor utama yang mempengaruhi resign karyawan.
3. Belum adanya sistem monitoring attrition yang mudah dipahami oleh departemen HR.
4. Perusahaan membutuhkan model prediksi untuk membantu mendeteksi karyawan yang berpotensi resign.

### Cakupan Proyek

Cakupan proyek yang dikerjakan meliputi:

1. Melakukan eksplorasi dan analisis data karyawan.
2. Membersihkan dan melakukan preprocessing data.
3. Melakukan visualisasi data untuk memahami pola attrition.
4. Membangun model machine learning menggunakan Random Forest.
5. Mengevaluasi performa model prediksi attrition.
6. Membuat business dashboard menggunakan Metabase.
7. Melakukan deployment model secara lokal menggunakan Python.

### Persiapan

Sumber data:
https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

Setup environment:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Business Dashboard

Business dashboard dibuat menggunakan Metabase untuk membantu departemen HR memahami dan memonitor faktor-faktor yang mempengaruhi attrition karyawan.

Dashboard menampilkan beberapa insight utama seperti:
- Attrition rate perusahaan
- Pengaruh overtime terhadap attrition
- Distribusi attrition berdasarkan department dan job role
- Hubungan monthly income dan job satisfaction terhadap attrition

### Menjalankan Dashboard Metabase

Versi Metabase yang digunakan:

```bash
metabase:v0.46.4
```

1. Jalankan container metabase pada docker
```bash
docker run -d -p 3000:3000 --name metabase metabase/metabase:v0.46.4
```
2. Copy file dashboard ke dalam container
```bash
docker cp metabase.db.mv.db metabase:/metabase.db/metabase.db.mv.db
```
3. Restart container
```bash
docker restart metabase
```
4. Akses dashboard melalui browser
```bash
http://localhost:3000
```
login: 
email: root@mail.com
password: root123


## Conclusion

Berdasarkan hasil eksplorasi data dan dashboard, ditemukan beberapa karakteristik yang berkaitan dengan tingkat attrition yang lebih tinggi.

Karyawan yang sering bekerja lembur terlihat memiliki proporsi attrition yang lebih tinggi dibandingkan karyawan yang tidak lembur. Selain itu, attrition juga lebih banyak ditemukan pada beberapa job role tertentu serta pada karyawan dengan tingkat kepuasan kerja dan work-life balance yang lebih rendah.

Hasil visualisasi pada dashboard dan exploratory data analysis (EDA) menunjukkan bahwa pola attrition lebih banyak ditemukan pada karyawan dengan overtime tinggi, job satisfaction rendah, serta pada beberapa job role tertentu.

Distribusi monthly income juga menunjukkan bahwa attrition lebih banyak terjadi pada kelompok karyawan dengan pendapatan rendah hingga menengah.

Model Random Forest yang dibangun berhasil mencapai performa yang cukup baik dengan accuracy sekitar 83% dan peningkatan recall pada kelas attrition setelah dilakukan penanganan imbalance data.

Business dashboard yang dibuat juga membantu departemen HR dalam memahami pola attrition secara visual sehingga dapat mendukung pengambilan keputusan yang lebih efektif.

Selain itu, model machine learning telah disimpan menggunakan `joblib` dan dapat digunakan kembali untuk melakukan prediksi attrition melalui file `predict.py`.

File yang disertakan dalam submission:
- `model.pkl`
- `preprocessor.pkl`
- `prediction.py`
- `metabase.db.mv.db`

Cara menjalankan prediksi:

```bash
python prediction.py
```

### Rekomendasi Action Items

- Mengurangi beban lembur untuk meningkatkan work-life balance karyawan.
- Meningkatkan kepuasan kerja melalui perbaikan lingkungan kerja.
- Meninjau kembali sistem kompensasi dan benefit.
- Memberikan perhatian lebih kepada karyawan baru atau dengan pengalaman kerja rendah.
- Mengembangkan strategi retensi untuk kelompok karyawan berisiko tinggi.