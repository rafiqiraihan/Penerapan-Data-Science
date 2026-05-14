# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Hingga saat ini institusi tersebut telah menghasilkan banyak lulusan dengan reputasi yang baik. Namun, masih terdapat cukup banyak mahasiswa yang tidak menyelesaikan pendidikannya atau mengalami dropout.

Tingginya angka dropout menjadi salah satu permasalahan penting karena dapat memengaruhi kualitas institusi, efektivitas pembelajaran, serta reputasi universitas. Oleh karena itu, pada proyek ini dibangun sistem machine learning untuk membantu mendeteksi mahasiswa yang berpotensi dropout lebih awal sehingga pihak universitas dapat memberikan pendampingan atau bimbingan khusus.

---

## Permasalahan Bisnis

Permasalahan bisnis yang ingin diselesaikan antara lain:

1. Tingginya angka dropout mahasiswa.
2. Sulit mengetahui faktor utama yang mempengaruhi dropout.
3. Belum tersedia dashboard monitoring dropout yang mudah dipahami.
4. Universitas membutuhkan sistem prediksi untuk mendeteksi mahasiswa yang berisiko dropout.

---

## Cakupan Proyek

Cakupan proyek yang dikerjakan meliputi:

1. Melakukan eksplorasi dan analisis data mahasiswa.
2. Melakukan preprocessing data.
3. Membuat visualisasi data untuk memahami pola dropout mahasiswa.
4. Membangun model machine learning menggunakan Random Forest.
5. Mengevaluasi performa model prediksi dropout.
6. Membuat business dashboard menggunakan Metabase.
7. Melakukan deployment prototype machine learning menggunakan Streamlit.

---

## Persiapan

### Sumber Data

Dataset:
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md

---

### Setup Environment

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

---

## Business Dashboard

Business dashboard dibuat menggunakan Metabase untuk membantu pihak universitas memahami dan memonitor faktor-faktor yang berkaitan dengan status dropout mahasiswa.

Dashboard menampilkan beberapa insight utama seperti:

* Jumlah mahasiswa berdasarkan status dropout
* Pengaruh nilai semester 1 terhadap dropout
* Pengaruh nilai semester 2 terhadap dropout
* Pengaruh jumlah mata kuliah lulus semester 1 terhadap dropout
* Pengaruh jumlah mata kuliah lulus semester 2 terhadap dropout
* Pengaruh pembayaran uang kuliah terhadap dropout

### Link Dashboard

http://localhost:3000/public/dashboard/b10ce703-3188-4711-9cb8-8f37718ca52a

---

## Menjalankan Sistem Machine Learning

Prototype machine learning dibuat menggunakan Streamlit untuk memprediksi kemungkinan mahasiswa mengalami dropout berdasarkan data akademik mahasiswa.

### Cara Menjalankan Secara Lokal

```bash
streamlit run app.py
```

### Input Prototype

Beberapa input yang digunakan dalam sistem prediksi antara lain:

* Age at Enrollment
* Admission Grade
* Previous Qualification Grade
* Semester 1 Grade
* Semester 2 Grade
* Semester 1 Approved Units
* Semester 2 Approved Units
* Debtor Status
* Tuition Fees Status

### Output Prototype

Sistem akan memberikan hasil prediksi:

* High Risk of Dropout
* Low Risk of Dropout

beserta probabilitas prediksi dropout mahasiswa.

### Link Prototype Streamlit

https://studentdoprediction.streamlit.app/

---

## Conclusion

Berdasarkan hasil exploratory data analysis (EDA) dan dashboard, ditemukan beberapa faktor yang memiliki hubungan kuat terhadap status dropout mahasiswa.

Mahasiswa dengan nilai semester 1 dan semester 2 yang rendah cenderung memiliki risiko dropout lebih tinggi dibandingkan mahasiswa dengan performa akademik yang baik. Rata-rata mahasiswa yang mengalami dropout memiliki nilai sekitar 6–8 dari skala 20.

Selain itu, jumlah mata kuliah yang berhasil diselesaikan pada semester pertama dan kedua juga menjadi faktor penting. Mahasiswa yang dropout rata-rata hanya menyelesaikan sekitar 2–3 mata kuliah.

Hasil feature importance dari model Random Forest menunjukkan bahwa faktor akademik seperti:

* jumlah mata kuliah lulus,
* nilai semester,
* pembayaran uang kuliah,

merupakan faktor yang paling memengaruhi prediksi dropout mahasiswa.

Model Random Forest yang dibangun berhasil mencapai performa yang cukup baik dengan accuracy sekitar 90%.

Business dashboard yang dibuat juga membantu pihak universitas memahami pola dropout secara visual sehingga dapat mendukung pengambilan keputusan yang lebih cepat dan efektif.

---

## Rekomendasi Action Items

Beberapa rekomendasi yang dapat dilakukan universitas berdasarkan hasil analisis adalah:

1. Memberikan pendampingan akademik lebih awal kepada mahasiswa dengan nilai semester rendah.
2. Melakukan monitoring khusus terhadap mahasiswa yang memiliki sedikit mata kuliah lulus pada semester awal.
3. Memberikan perhatian tambahan kepada mahasiswa yang memiliki tunggakan pembayaran kuliah.
4. Mengembangkan sistem early warning berbasis machine learning untuk mendeteksi mahasiswa berisiko dropout secara berkala.
5. Memanfaatkan dashboard monitoring untuk membantu pengambilan keputusan akademik secara lebih cepat dan terukur.
