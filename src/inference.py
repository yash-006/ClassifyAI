# ==========================================
# Inference Module
# ==========================================

"""
Inference utilities for ClassifyAI.

Supports:
- Animals
- Butterflies
- ImageNet10

Models:
- AlexNet
- VGG16
- VGG19
- ResNet18
- ResNet34
- SEResNet50
- ConvNeXt
"""

# ==========================================
# Imports
# ==========================================

import json
import time
import sys
from pathlib import Path

import torch
from PIL import Image
from torchvision import transforms

sys.path.append(str(Path(__file__).resolve().parent))

from model_factory import create_model

# ==========================================
# Project Paths
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CHECKPOINT_DIR = PROJECT_ROOT / "checkpoints"

MODEL_DIR = PROJECT_ROOT / "models"

IMAGE_SIZE = 224

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# ==========================================
# Image Transform
# ==========================================

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

transform = transforms.Compose([

    transforms.Resize(256),

    transforms.CenterCrop(IMAGE_SIZE),

    transforms.ToTensor(),

    transforms.Normalize(
        IMAGENET_MEAN,
        IMAGENET_STD
    )
])

# ==========================================
# Load Class Mapping
# ==========================================

def load_class_mapping(dataset):

    mapping_file = (
        MODEL_DIR
        / dataset
        / "class_to_idx.json"
    )

    with open(mapping_file, "r") as file:

        class_to_idx = json.load(file)

    idx_to_class = {
        value: key
        for key, value in class_to_idx.items()
    }

    return idx_to_class

# ==========================================
# Load Trained Model
# ==========================================

def load_model(
    dataset,
    model_name
):

    idx_to_class = load_class_mapping(dataset)

    num_classes = len(idx_to_class)

    model = create_model(
        model_name=model_name,
        num_classes=num_classes,
        pretrained=False
    )

    checkpoint_path = (
        CHECKPOINT_DIR
        / dataset
        / f"{model_name}_best.pth"
    )

    checkpoint = torch.load(
        checkpoint_path,
        map_location=DEVICE,
        weights_only=False
    )

    model.load_state_dict(
        checkpoint["model_state_dict"]
    )

    model.to(DEVICE)

    model.eval()

    return model, idx_to_class

# ==========================================
# Preprocess Image
# ==========================================

def preprocess_image(image_path):

    image = Image.open(image_path)

    image = image.convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    return image.to(DEVICE)

# ==========================================
# Predict Image
# ==========================================

def predict_image(
    image_path,
    dataset,
    model_name
):

    model, idx_to_class = load_model(
        dataset,
        model_name
    )

    image = preprocess_image(image_path)

    start = time.perf_counter()

    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(
            outputs,
            dim=1
        )

    end = time.perf_counter()

    confidence, prediction = torch.max(
        probabilities,
        dim=1
    )

    predicted_class = idx_to_class[
        prediction.item()
    ]

    inference_time = (
        end - start
    ) * 1000

    return {

   	"dataset": dataset,

    	"model": model_name,

    	"prediction": predicted_class,

    	"confidence": confidence.item(),
	
    	"inference_time_ms": inference_time
    }

# ==========================================
# Top-5 Predictions
# ==========================================

def top5_predictions(
    image_path,
    dataset,
    model_name
):

    model, idx_to_class = load_model(
        dataset,
        model_name
    )

    image = preprocess_image(image_path)

    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(
            outputs,
            dim=1
        )

    values, indices = torch.topk(
        probabilities,
        k=min(5, probabilities.shape[1])
    )

    results = []

    for value, index in zip(
        values[0],
        indices[0]
    ):

        results.append({

            "class": idx_to_class[
                index.item()
            ],

            "confidence": value.item()

        })

    return results