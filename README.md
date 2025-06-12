# Tomato Leaf Disease Detection

![Tomato Leaf Detection](assets/tomato_leaf_detection_banner.png)
*(Anda bisa mengganti `assets/tomato_leaf_detection_banner.png` dengan gambar yang relevan dari proyek Anda, atau hapus baris ini jika tidak ada gambar.)*

Proyek ini bertujuan untuk mendeteksi penyakit pada daun tomat menggunakan model *deep learning*. Deteksi dini penyakit sangat penting untuk menjaga kesehatan tanaman tomat dan memaksimalkan hasil panen. Aplikasi ini dibangun menggunakan Flask untuk antarmuka web.

## Fitur

* **Klasifikasi Penyakit Daun Tomat:** Mampu mengidentifikasi berbagai jenis penyakit yang menyerang daun tomat.
* **Penggunaan Model *Deep Learning*:** Memanfaatkan arsitektur jaringan saraf konvolusi (CNN) untuk akurasi yang tinggi.
* **Antarmuka Web Sederhana:** Aplikasi berbasis web menggunakan Flask untuk memudahkan interaksi pengguna.
* **Basis Data Gambar Daun Tomat:** Model dilatih menggunakan koleksi gambar daun tomat yang sehat dan yang terinfeksi.

## Model

Model *deep learning* yang digunakan dalam proyek ini disimpan dalam format `.h5`. Model ini telah dilatih untuk mengidentifikasi berbagai kondisi daun tomat.

**Lokasi Model:** Anda dapat mengunduh model `.h5` dari tautan Google Drive berikut:

* **[Tomato Leaf Detection Model (.h5)](https://drive.google.com/file/d/1c3TgLesAlRYABXC6vkscOEUlYyZZvL3S/view?usp=sharing)**

Setelah diunduh, pastikan file model bernama `Tomato_Models.h5` dan diletakkan di direktori utama proyek, sejajar dengan `app.py`.

## Instalasi

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah di bawah ini:

1.  **Kloning Repositori:**
    ```bash
    git clone [https://github.com/RolandSitompul750/Tomato-Leaf-Detection.git](https://github.com/RolandSitompul750/Tomato-Leaf-Detection.git)
    cd Tomato-Leaf-Detection
    ```

2.  **Buat Virtual Environment (opsional, tapi disarankan):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk Linux/macOS
    # venv\Scripts\activate   # Untuk Windows
    ```

3.  **Instal Dependensi:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Pastikan Anda memiliki file `requirements.txt` yang berisi semua dependensi yang diperlukan seperti `flask`, `tensorflow`, `keras`, `numpy`, `opencv-python`, dll. Jika belum ada, Anda bisa membuatnya secara manual atau menggunakan `pip freeze > requirements.txt` setelah menginstal semua library yang Anda gunakan.)*

4.  **Unduh Model:** Unduh file model `Tomato_Models.h5` dari tautan Google Drive yang disediakan di bagian [Model](#model) dan letakkan di direktori utama proyek (sejajar dengan `app.py`).

## Penggunaan

Setelah instalasi dan model diunduh, Anda dapat menjalankan aplikasi web Flask:

1.  **Jalankan Aplikasi Flask:**
    ```bash
    flask --app app.py run
    ```

2.  **Akses Aplikasi:** Buka browser web Anda dan kunjungi alamat yang diberikan oleh Flask, biasanya `http://127.0.0.1:5000/`.

Anda kemudian dapat mengunggah gambar daun tomat melalui antarmuka web untuk mendapatkan diagnosis.

## Struktur Proyek

Berikut adalah gambaran struktur direktori proyek ini:

├── pycache/  
│   └── app.cpython-312.pyc  
├── static/  
│   └── css/  
│       └── custom.css  
├── templates/  
│   ├── index.html  
│   ├── layout.html  
│   └── result.html  
├── Tomato_Models.h5  
├── app.py  
└── requirements.txt  
└── README.md  
