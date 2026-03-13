import os
import shutil

dataset_dir = r"c:\Users\guhan\OneDrive\Pictures\plant-ai\dataset"
plant_village = os.path.join(dataset_dir, "PlantVillage")

# 1. remove PlantVillage if exists
if os.path.exists(plant_village):
    shutil.rmtree(plant_village)

# 2. rename map
rename_map = {
    "Pepper__bell___Bacterial_spot": "Pepper,_bell___Bacterial_spot",
    "Pepper__bell___healthy": "Pepper,_bell___healthy",
    "Potato___Early_blight": "Potato___Early_blight",
    "Potato___Late_blight": "Potato___Late_blight",
    "Potato___healthy": "Potato___healthy",
    "Tomato_Bacterial_spot": "Tomato___Bacterial_spot",
    "Tomato_Early_blight": "Tomato___Early_blight",
    "Tomato_Late_blight": "Tomato___Late_blight",
    "Tomato_Leaf_Mold": "Tomato___Leaf_Mold",
    "Tomato_Septoria_leaf_spot": "Tomato___Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite": "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato__Target_Spot": "Tomato___Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus": "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato__Tomato_mosaic_virus": "Tomato___Tomato_mosaic_virus",
    "Tomato_healthy": "Tomato___healthy"
}

for old_name, new_name in rename_map.items():
    old_path = os.path.join(dataset_dir, old_name)
    new_path = os.path.join(dataset_dir, new_name)
    if os.path.exists(old_path) and not os.path.exists(new_path):
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")

# Print final folders sorted
print("Final classes in order:")
classes = sorted(os.listdir(dataset_dir))
for c in classes:
    print(c)
