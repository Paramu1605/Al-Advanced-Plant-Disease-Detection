# Plant-AI 🌿

Plant-AI is an intelligent web application that helps farmers, gardeners, and plant enthusiasts identify plant diseases from images. Simply upload an image of a plant leaf, and the application will use a deep learning model to predict the disease and provide tailored information on how to prevent or cure it.

## Features ✨
- **Image Upload:** Easy-to-use web interface for uploading pictures of plant leaves.
- **Disease Prediction:** Uses a PyTorch-based **ResNet34** deep learning architecture to classify the image into one of 15 different plant/disease classes (such as Bell Pepper Bacterial Spot, Potato Early Blight, Tomato Yellow Leaf Curl Virus, etc.).
- **Actionable Advice:** Provides detailed information about the predicted disease, including its causes and actionable steps for prevention and cure.
- **Responsive UI:** Web interface built using HTML/CSS, making it accessible on both desktop and mobile devices.

## Tech Stack 🛠️
- **Backend:** Python, Flask
- **Machine Learning:** PyTorch, Torchvision 
- **Frontend:** HTML, CSS, Bootstrap

## Setup & Installation 🚀

1. **Clone or Download the Repository**
   Ensure you have the project files locally on your machine.

2. **Set up a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   Install the necessary Python packages (PyTorch, Flask, Pillow, etc.):
   ```bash
   pip install torch torchvision flask pillow
   ```
   *(Note: Depending on your system, you might want to install PyTorch with GPU support if you have a compatible NVIDIA GPU, though CPU works perfectly fine for inference.)*

4. **Prepare the Model**
   The application relies on a trained `plantDisease-resnet34.pth` model file located in the `Models/` folder. If you want to retrain the model on your dataset:
   - Ensure your data is organized inside the `dataset/` folder.
   - Run the dataset preparation script if needed.
   - Run the training script:
     ```bash
     cd Models
     python train_plant_model.py
     ```

## Usage 💡

1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to the local server, typically:
   ```
   http://127.0.0.1:5000
   ```
3. Upload an image of a plant leaf and click **Predict** to view the results.

## Model Classes 🏷️
The model is trained to recognize the following classes:
- Pepper (bell) - Bacterial spot
- Pepper (bell) - Healthy
- Potato - Early blight
- Potato - Late blight
- Potato - Healthy
- Tomato - Bacterial spot
- Tomato - Early blight
- Tomato - Late blight
- Tomato - Leaf Mold
- Tomato - Septoria leaf spot
- Tomato - Spider mites (Two-spotted spider mite)
- Tomato - Target Spot
- Tomato - Tomato Yellow Leaf Curl Virus
- Tomato - Tomato mosaic virus
- Tomato - Healthy

## Acknowledgments
- PlantVillage dataset used for training the model.
- Architecture utilizing ResNet34 from `torchvision.models`.
