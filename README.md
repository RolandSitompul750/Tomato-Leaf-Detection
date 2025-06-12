# Tomato Leaf Disease Detection

![Tomato Leaf Detection](https://github.com/RolandSitompul750/Tomato-Leaf-Detection/blob/main/assets/tomato_leaf_detection_banner.png?raw=true)
*(Anda bisa mengganti `assets/tomato_leaf_detection_banner.png` dengan gambar yang relevan dari proyek Anda, atau hapus baris ini jika tidak ada gambar.)*

Proyek ini bertujuan untuk mendeteksi penyakit pada daun tomat menggunakan model *deep learning*. Deteksi dini penyakit sangat penting untuk menjaga kesehatan tanaman tomat dan memaksimalkan hasil panen.

## Fitur

* **Klasifikasi Penyakit Daun Tomat:** Mampu mengidentifikasi berbagai jenis penyakit yang menyerang daun tomat.
* **Penggunaan Model *Deep Learning*:** Memanfaatkan arsitektur jaringan saraf konvolusi (CNN) untuk akurasi yang tinggi.
* **Basis Data Gambar Daun Tomat:** Dilatih menggunakan koleksi gambar daun tomat yang sehat dan yang terinfeksi.

## Model

Model *deep learning* yang digunakan dalam proyek ini disimpan dalam format `.h5`. Model ini telah dilatih untuk mengidentifikasi berbagai kondisi daun tomat.

**Lokasi Model:** Anda dapat mengunduh model `.h5` dari tautan Google Drive berikut:

* **[Tomato Leaf Detection Model (.h5)](https://drive.google.com/file/d/1c3TgLesAlRYABXC6vkscOEUlYyZZvL3S/view?usp=sharing)**

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
    *(Pastikan Anda memiliki file `requirements.txt` yang berisi semua dependensi yang diperlukan seperti `tensorflow`, `keras`, `numpy`, `opencv-python`, dll. Jika belum ada, Anda bisa membuatnya secara manual atau menggunakan `pip freeze > requirements.txt` setelah menginstal semua library.)*

4.  **Unduh Model:** Unduh file model `.h5` dari tautan Google Drive yang disediakan di bagian [Model](#model) dan letakkan di direktori proyek Anda (misalnya, di dalam folder `models/`).

## Penggunaan

Setelah instalasi, Anda dapat menggunakan proyek ini untuk melakukan prediksi pada gambar daun tomat.

*(Tambahkan instruksi spesifik tentang cara menjalankan skrip prediksi Anda. Contohnya:)*

1.  **Jalankan Skrip Prediksi:**
    ```bash
    python predict.py --image_path path/to/your/image.jpg --model_path path/to/your/model.h5
    ```
    *(Ganti `predict.py` dengan nama skrip utama Anda untuk prediksi, dan sesuaikan argumen `--image_path` serta `--model_path` sesuai dengan implementasi Anda.)*

## Struktur Proyek
