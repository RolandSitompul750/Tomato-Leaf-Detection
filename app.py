import os
from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# 1. Inisialisasi Flask App
app = Flask(__name__)

# 2. Definisi Konstan (IMAGE_SIZE, CLASS_NAMES)
IMAGE_SIZE = (300, 300)
CLASS_NAMES = [
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# 3. Pemuatan Model Global
# Pastikan model dimuat hanya sekali saat aplikasi dimulai
try:
    model = load_model("Tomato_Models.h5")
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    print("Model 'Tomato_Models.h5' berhasil dimuat.")
except Exception as e:
    print(f"Error saat memuat model: {e}")
    model = None

# 4. Definisi Fungsi Pra-pemrosesan Gambar
# Fungsi ini perlu didefinisikan sebelum dipanggil oleh fungsi lain
def preprocess_img(img_stream):
    img_stream.seek(0) # Penting: Reset stream ke awal
    op_img = Image.open(img_stream)
    img_resize = op_img.resize(IMAGE_SIZE)
    img2arr = image.img_to_array(img_resize) / 255.0
    print(f"Shape setelah img_to_array: {img2arr.shape}") # Debugging
    img_reshape = img2arr.reshape(1, *IMAGE_SIZE, 3)
    
    return img_reshape

# 5. Definisi Fungsi Prediksi
# Fungsi ini juga perlu didefinisikan sebelum dipanggil oleh fungsi lain
def predict_result(processed_img_array):
    if model is None:
        raise ValueError("Model tidak dimuat. Tidak dapat melakukan prediksi.")
    
    pred_raw = model.predict(processed_img_array)
    predicted_class_index = np.argmax(pred_raw[0], axis=-1)
    predicted_class_name = CLASS_NAMES[predicted_class_index]
    confidence = pred_raw[0][predicted_class_index]
    return predicted_class_name, confidence

# 6. Definisi Home Route
@app.route("/")
def main():
    return render_template("index.html")

# 7. Definisi Prediction Route
# Route ini memanggil preprocess_img dan predict_result
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    if model is None:
        return render_template("result.html", err="Model tidak dimuat. Silakan periksa log server.")

    try:
        if request.method == 'POST':
            uploaded_file = request.files['file']
            if uploaded_file.filename == '':
                raise ValueError("Tidak ada file yang dipilih.")

            print(f"File diterima di backend: {uploaded_file.filename}")

            # Pra-proses gambar
            processed_img_array = preprocess_img(uploaded_file.stream)

            # Lakukan prediksi
            predictions_raw = model.predict(processed_img_array) # Lakukan prediksi sekali

            # Debugging: Cetak prediksi mentah dari model (semua probabilitas)
            print(f"Prediksi mentah dari model: {predictions_raw[0]}")

            predicted_class_index = np.argmax(predictions_raw[0])
            predicted_class_name = CLASS_NAMES[predicted_class_index]
            confidence = float(predictions_raw[0][predicted_class_index]) # Gunakan hasil prediksi yang sama

            print(f"Kelas terprediksi: {predicted_class_name}, Kepercayaan: {confidence}")

            return render_template("result.html",
                                   predictions=f"Penyakit: {predicted_class_name}",
                                   confidence=f"Kepercayaan: {confidence*100:.2f}%")

    except Exception as e:
        error_message = f"File tidak dapat diproses atau terjadi kesalahan: {str(e)}"
        print(f"Terjadi error di prediksi: {error_message}")
        return render_template("result.html", err=error_message)

#  Driver Code
if __name__ == "__main__":
    app.run(port=5000, debug=True)