import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import io

# ==========================
# CONFIG
# ==========================
st.set_page_config(page_title="Construction Safety Detection", layout="wide")

MODEL_PATH = r"E:\Purwadhika\Coding\Capstone Project 4\weights\best.pt"
model = YOLO(MODEL_PATH)

# ==========================
# STYLE
# ==========================
st.markdown(
    """
    <h1 style='text-align:center; color:white;'>🦺 Construction Safety Object Detection</h1>
    <p style='text-align:center; color:#cccccc;'>Upload gambar pekerja konstruksi untuk mendeteksi APD (helmet, vest, no-vest).</p>
    <br>
    """,
    unsafe_allow_html=True,
)

# =====================================
# IMAGE UPLOAD
# =====================================
uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"],
    help="Upload foto pekerja konstruksi"
)

# Slider confidence
conf_thres = st.slider(
    "Confidence Threshold",
    0.10, 0.90, 0.30, 0.05,
    help="Semakin rendah, semakin banyak objek yang terdeteksi"
)

if uploaded_file is not None:

    # --------------------
    # 1. READ IMAGE
    # --------------------
    img = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(img)

    st.image(img, caption="Original Image", use_column_width=True)

    # --------------------
    # 2. PREDICT
    # --------------------
    results = model.predict(img_np, conf=conf_thres)

    # --------------------
    # 3. BETTER PLOT (anti-crop)
    # --------------------
    plot = results[0].plot()  # numpy array (BGR)
    plot_rgb = Image.fromarray(plot[..., ::-1])  # BGR → RGB (tanpa cv2)

    st.subheader("🔍 Detection Result")
    st.image(plot_rgb, use_column_width=True)

    # --------------------
    # 4. COUNT OBJECTS
    # --------------------
    names = model.names
    obj_count = {}

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = names[cls_id]
        obj_count[label] = obj_count.get(label, 0) + 1

    st.subheader("📊 Object Count Result")
    st.json(obj_count)

    # --------------------
    # 5. SAFETY ANALYSIS
    # --------------------
    st.subheader("🧯 Safety Compliance Analysis")

    total = obj_count.get("person", 0)
    helmet = obj_count.get("helmet", 0)
    vest = obj_count.get("vest", 0)
    no_vest = obj_count.get("no-vest", 0)

    # Hitung pekerja tanpa helmet
    no_helmet = total - helmet

    # Display
    st.write(f"• **Total Worker:** {total}")
    st.write(f"• **Worker wearing Helmet:** {helmet}")
    st.write(f"• **Worker wearing Vest:** {vest}")
    st.write(f"• **Worker WITHOUT Vest:** {no_vest}")
    st.write(f"• **Worker WITHOUT Helmet:** {no_helmet}")

    # ---- STATUS ALERT ----
    if no_helmet > 0 and no_vest > 0:
        st.error("❗ Ada pekerja yang TIDAK memakai helmet dan safety vest!")
    elif no_helmet > 0:
        st.error("❗ Ada pekerja yang TIDAK memakai helmet!")
    elif no_vest > 0:
        st.error("❗ Ada pekerja yang TIDAK memakai safety vest!")
    else:
        st.success("✔ Semua pekerja memakai alat keselamatan dengan lengkap.")