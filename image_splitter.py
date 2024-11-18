from PIL import Image
import os
from tkinter import Tk, filedialog

def split_images_and_save():
    # Dosya seçim penceresi
    Tk().withdraw()  # Tkinter ana penceresini gizle
    file_paths = filedialog.askopenfilenames(title="Resimleri Seçin", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    
    if not file_paths:
        print("Hiçbir dosya seçilmedi.")
        return

    # Çıktı klasörünü seç
    output_folder = filedialog.askdirectory(title="Çıktı Klasörünü Seç")
    if not output_folder:
        print("Çıktı klasörü seçilmedi.")
        return

    for file_path in file_paths:
        try:
            image = Image.open(file_path)
            width, height = image.size
            piece_width = width // 2
            piece_height = height // 2

            # Dosya adı ve uzantı bilgisi
            base_name = os.path.splitext(os.path.basename(file_path))[0]

            # Dört parçayı oluştur ve kaydet
            for i in range(2):
                for j in range(2):
                    left = j * piece_width
                    upper = i * piece_height
                    right = left + piece_width
                    lower = upper + piece_height

                    # Parçayı kırp
                    cropped_image = image.crop((left, upper, right, lower))

                    # Yeni dosya adı ve numaralandırma
                    output_name = f"{base_name}_{i*2+j+1:02d}.webp"
                    output_path = os.path.join(output_folder, output_name)

                    # WebP formatında kaydet
                    cropped_image.save(output_path, format="WEBP")
            
            print(f"{base_name} dosyası başarıyla işlendi.")
        except Exception as e:
            print(f"Hata oluştu: {file_path} - {e}")

    print("Tüm dosyalar işlendi.")

# Fonksiyonu çağır
split_images_and_save()
