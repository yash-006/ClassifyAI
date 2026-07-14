
import torch.nn as nn
import timm

from torchvision.models import (
    alexnet,
    vgg16,
    vgg19,
    resnet18,
    resnet34,
    convnext_tiny,

    AlexNet_Weights,
    VGG16_Weights,
    VGG19_Weights,
    ResNet18_Weights,
    ResNet34_Weights,
    ConvNeXt_Tiny_Weights
)

def create_model(model_name, num_classes, pretrained=True):

    if model_name == "alexnet":

        model = alexnet(
            weights=AlexNet_Weights.DEFAULT if pretrained else None
        )

        model.classifier[6] = nn.Linear(
            model.classifier[6].in_features,
            num_classes
        )

    elif model_name == "vgg16":

        model = vgg16(
            weights=VGG16_Weights.DEFAULT if pretrained else None
        )

        model.classifier[6] = nn.Linear(
            model.classifier[6].in_features,
            num_classes
        )

    elif model_name == "vgg19":

        model = vgg19(
            weights=VGG19_Weights.DEFAULT if pretrained else None
        )

        model.classifier[6] = nn.Linear(
            model.classifier[6].in_features,
            num_classes
        )

    elif model_name == "resnet18":

        model = resnet18(
            weights=ResNet18_Weights.DEFAULT if pretrained else None
        )

        model.fc = nn.Linear(
            model.fc.in_features,
            num_classes
        )

    elif model_name == "resnet34":

        model = resnet34(
            weights=ResNet34_Weights.DEFAULT if pretrained else None
        )

        model.fc = nn.Linear(
            model.fc.in_features,
            num_classes
        )
        
    elif model_name == "seresnet50":

        model = timm.create_model(
            "seresnet50",
            pretrained=pretrained
        )
    
        model.fc = nn.Linear(
            model.fc.in_features,
            num_classes
        )

    elif model_name == "convnext":

        model = convnext_tiny(
            weights=ConvNeXt_Tiny_Weights.DEFAULT if pretrained else None
        )

        model.classifier[2] = nn.Linear(
            model.classifier[2].in_features,
            num_classes
        )

    else:

        raise ValueError(f"Unsupported model: {model_name}")

    return model
