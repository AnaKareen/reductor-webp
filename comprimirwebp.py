from PIL import Image
import os

input_folder = r"C:\Users\20030\Downloads\Nueva carpeta\Nueva carpeta"
output_folder = r"C:\Users\20030\Desktop\PORTFOLIO\static\img\photography"

os.makedirs(output_folder, exist_ok=True)

quality = 70  # 60–80 recomendado para web

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".webp"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        img = Image.open(input_path)
        img.save(output_path, "WEBP", quality=quality, method=6)

        print(f"Optimizada: {filename}")
