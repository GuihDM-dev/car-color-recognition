import streamlit as st
from PIL import Image
from ultralytics import YOLO

# Carregue o modelo
model = YOLO(r"C:\Users\guilh\OneDrive\Documentos\GitHub\car-color-recognition\notebooks\vehicle_car_color_yolov8n.pt")  # Substitua pelo seu modelo treinado

st.title("Reconhecimento de Cores de Carros")
st.write("Este projeto utiliza YOLOv8 para detectar e classificar cores de carros. /n Cores aceitas Branco, Preto, Vermelho, Amarelo, Prata, Azul e Verde")

# Upload de imagem
uploaded_file = st.file_uploader("Carregue uma imagem", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Exiba a imagem carregada
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem carregada", use_column_width=True)

    # Faça a predição
    st.write("Processando a imagem...")
    results = model(image)

    # Exiba os resultados
    st.write("### Resultados:")
    for r in results:
        for box in r.boxes:
            # Converta o tensor para um valor numérico
            st.write(f"Classe: {int(box.cls)}, Confiança: {float(box.conf):.2f}")


    # Visualize a imagem com predições
    annotated_image = results[0].plot()
    st.image(annotated_image, caption="Predições do modelo", use_column_width=True)
