import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="Garbage Detection AI",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("♻️ Smart Waste Classification System")
st.markdown("""
### Powered by YOLOv8
Sistem ini menggunakan Artificial Intelligence untuk mendeteksi dan mengklasifikasikan sampah 
ke dalam 6 kategori: **Biodegradable, Cardboard, Glass, Metal, Paper, dan Plastic**.
""")

st.sidebar.header("⚙️ Model Configuration")

conf_threshold = st.sidebar.slider(
    "Confidence Threshold", 
    min_value=0.0, 
    max_value=1.0, 
    value=0.25, 
    step=0.05,
    help="Atur seberapa yakin model harus mendeteksi objek."
)

st.sidebar.markdown("---")
st.sidebar.info(
    "**Developer Note:**\n"
    "Project ini dibuat untuk mendemonstrasikan kemampuan Computer Vision "
    "menggunakan arsitektur YOLOv8 pada custom dataset."
)

@st.cache_resource
def load_model(model_path):
    return YOLO(model_path)

try:
    model = load_model("best.pt")
    st.sidebar.success("✅ Model Loaded Successfully")
except Exception as e:
    st.error(f"Gagal memuat model. Pastikan file 'best.pt' ada. Error: {e}")
    st.stop()

uploaded_file = st.file_uploader("Upload foto sampah di sini...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # 1. Buka gambar dengan PIL
    image = Image.open(uploaded_file)
    
    # 2. Bagi kolom untuk tampilan Before/After
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📸 Original Image")
        st.image(image, use_column_width=True)

    # 3. Tombol Deteksi
    if st.sidebar.button("🔍 Detect Waste", type="primary"):
        with st.spinner("Sedang menganalisis gambar..."):
            # 4. PROSES INFERENSI
            results = model.predict(image, conf=conf_threshold)
            
            # 5. Ambil hasil plot 
            res_plotted = results[0].plot()
            
            # Convert BGR ke RGB agar warna tidak aneh di Streamlit
            res_plotted_rgb = res_plotted[:, :, ::-1]

    with col2:
        st.subheader("🤖 AI Detection Result")
        if 'res_plotted_rgb' in locals():
            st.image(res_plotted_rgb, caption="Predicted Output", use_column_width=True)
            
            st.success("Deteksi Selesai!")
            
            boxes = results[0].boxes
            if len(boxes) > 0:
                st.markdown("**Objek Terdeteksi:**")
                for box in boxes:
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    name = model.names[cls]
                    st.write(f"- **{name}**: {conf:.2f} confidence")
            else:
                st.warning("Tidak ada objek sampah yang terdeteksi dengan threshold ini.")

else:
    # Tampilan default jika belum upload
    st.info("Silakan upload gambar untuk memulai.")
