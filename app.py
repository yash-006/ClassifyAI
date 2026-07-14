# ==========================================
# ClassifyAI Streamlit App
# ==========================================

import sys
from pathlib import Path

import streamlit as st

# ==========================================
# Project Paths
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent

sys.path.append(str(PROJECT_ROOT / "src"))

from inference import (
    predict_image,
    top5_predictions
)

# ==========================================
# Streamlit Page Config
# ==========================================

st.set_page_config(
    page_title="ClassifyAI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Header
# ==========================================

st.title("🧠 ClassifyAI")

st.markdown(
    """
### AI-Powered Image Classification

This application uses **Transfer Learning** with **ConvNeXt Tiny**
to classify images from multiple datasets.

Select a dataset, upload an image and click **Predict**.
"""
)

st.divider()

# ==========================================
# Sidebar
# ==========================================

st.sidebar.header("⚙ Settings")

dataset = st.sidebar.selectbox(
    "Select Dataset",
    [
        "animals",
        "butterflies",
        "imagenet10"
    ]
)

BEST_MODELS = {
    "animals": "convnext",
    "butterflies": "convnext",
    "imagenet10": "convnext"
}

model = BEST_MODELS[dataset]

st.sidebar.success("🏆 Best Model")

st.sidebar.info("ConvNeXt Tiny")

st.sidebar.divider()

st.sidebar.markdown(
    f"""
**Dataset**

{dataset.title()}

---

**Model**

ConvNeXt Tiny
"""
)

# ==========================================
# Upload Image
# ==========================================

uploaded_file = st.file_uploader(
    "📤 Upload an Image",
    type=["jpg", "jpeg", "png"]
)

# Stop here until user uploads image
if uploaded_file is None:

    st.info("👆 Upload an image to begin prediction.")

    st.stop()

# Save Uploaded Image

image_path = PROJECT_ROOT / "temp_image.jpg"

with open(image_path, "wb") as file:
    file.write(uploaded_file.getbuffer())

st.divider()

# ==========================================
# Preview Layout
# ==========================================

left_col, right_col = st.columns([1.2, 1])

with left_col:

    st.subheader("🖼 Uploaded Image")

    st.image(
        uploaded_file,
        use_container_width=True
    )

with right_col:

    st.subheader("🚀 Ready to Predict")

    st.write("Dataset")

    st.success(dataset.title())

    st.write("Model")

    st.success("ConvNeXt Tiny")

    predict = st.button(
        "🔍 Predict",
        use_container_width=True,
        type="primary"
    )

if not predict:
    st.stop()

# ==========================================
# Run Prediction
# ==========================================

with st.spinner("Running inference..."):

    try:

        result = predict_image(
            image_path=image_path,
            dataset=dataset,
            model_name=model
        )

        top5 = top5_predictions(
            image_path=image_path,
            dataset=dataset,
            model_name=model
        )

    except Exception as error:

        st.error(f"❌ {error}")

        st.stop()

st.divider()

# ==========================================
# Results
# ==========================================

st.subheader("🎯 Prediction Results")

metric1, metric2, metric3 = st.columns(3)

with metric1:

    st.metric(
        label="Prediction",
        value=result["prediction"]
    )

with metric2:

    st.metric(
        label="Confidence",
        value=f"{result['confidence']*100:.2f}%"
    )

with metric3:

    st.metric(
        label="Inference Time",
        value=f"{result['inference_time_ms']:.2f} ms"
    )

st.divider()

# ==========================================
# Image + Prediction
# ==========================================

image_col, info_col = st.columns([1,1])

with image_col:

    st.subheader("🖼 Uploaded Image")

    st.image(
        uploaded_file,
        use_container_width=True
    )

with info_col:

    st.subheader("📋 Prediction Summary")

    st.write(f"**Dataset** : {dataset.title()}")

    st.write(f"**Model** : ConvNeXt Tiny")

    st.write(f"**Predicted Class** : {result['prediction']}")

    st.write(
        f"**Confidence** : {result['confidence']*100:.2f}%"
    )

    st.write(
        f"**Inference Time** : {result['inference_time_ms']:.2f} ms"
    )

# ==========================================
# Top-5 Predictions
# ==========================================

st.divider()

st.subheader("🏆 Top-5 Predictions")

for rank, prediction in enumerate(top5, start=1):

    confidence = float(prediction["confidence"])

    class_name = prediction["class"]

    st.markdown(f"### {rank}. {class_name}")

    st.progress(confidence)

    st.caption(f"{confidence*100:.2f}% Confidence")

st.divider()

# ==========================================
# Prediction Details
# ==========================================

with st.expander("📄 Prediction Details", expanded=False):

    details_col1, details_col2 = st.columns(2)

    with details_col1:

        st.write("**Dataset**")
        st.write(dataset.title())

        st.write("**Model**")
        st.write("ConvNeXt Tiny")

        st.write("**Predicted Class**")
        st.write(result["prediction"])

    with details_col2:

        st.write("**Confidence**")
        st.write(f"{result['confidence']*100:.2f}%")

        st.write("**Inference Time**")
        st.write(f"{result['inference_time_ms']:.2f} ms")

        st.write("**Framework**")
        st.write("PyTorch + Streamlit")

# ==========================================
# Model Information
# ==========================================

with st.expander("ℹ️ About This Model", expanded=False):

    st.markdown(
        """
### ConvNeXt Tiny

ConvNeXt Tiny is a modern Convolutional Neural Network inspired by
Vision Transformers while retaining the efficiency of CNNs.

It was selected because it achieved the highest overall performance
during comparative evaluation.

### Evaluation Metrics

- ✅ Accuracy
- ✅ Precision
- ✅ Recall
- ✅ Macro F1 Score
- ✅ Expected Calibration Error (ECE)
- ✅ Inference Time

### Framework

- PyTorch
- Torchvision
- Streamlit
        """
    )

st.divider()

# ==========================================
# Footer
# ==========================================

st.markdown(
    """
---
<div style="text-align:center">

### 🧠 ClassifyAI

AI-powered Image Classification using Transfer Learning

Developed using **PyTorch**, **Streamlit**, and **ConvNeXt Tiny**

</div>
""",
    unsafe_allow_html=True
)

# ==========================================
# Remove Temporary Image
# ==========================================

try:

    if image_path.exists():

        image_path.unlink()

except Exception:

    pass