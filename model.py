import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io


# Define model
# define model
model = models.resnet34()
model.fc = nn.Linear(model.fc.in_features, 15)


# Define transforms (resize + normalize for ResNet)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],  # Imagenet mean
                         [0.229, 0.224, 0.225])  # Imagenet std
])

# Class labels
num_classes = [
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
    'Potato___Late_blight', 'Potato___healthy', 'Tomato___Bacterial_spot',
    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
]

# Load trained model
model.load_state_dict(torch.load(
    './Models/plantDisease-resnet34.pth', map_location=torch.device('cpu')
))
model.eval()


# Prediction function
def predict_image(img_bytes):
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    tensor = transform(img).unsqueeze(0)  # add batch dimension
    with torch.no_grad():
        outputs = model(tensor)
        _, preds = torch.max(outputs, dim=1)
    return num_classes[preds.item()]
