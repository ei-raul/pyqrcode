import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# --- Configuração da Página ---
st.set_page_config(page_title="Gerador de QR Code HD", page_icon="📱")

st.title("📱 Gerador de QR Code em Alta Resolução")
st.markdown("Cole seu link abaixo e configure as cores e o tamanho para baixar sua imagem.")

# --- Barra Lateral de Configurações ---
with st.sidebar:
    st.header("🎨 Personalização")
    
    # Escolha de Cores
    col1, col2 = st.columns(2)
    with col1:
        fill_color = st.color_picker("Cor do QR", "#000000")
    with col2:
        back_color = st.color_picker("Cor do Fundo", "#ffffff")
    
    # Configuração de Resolução (Box Size)
    st.markdown("---")
    st.header("📐 Resolução")
    tamanho = st.slider(
        "Tamanho do Pixel (Box Size)",
        min_value=10,
        max_value=100,
        value=20,
        help="Quanto maior este número, maior a resolução final da imagem."
    )
    
    # Nível de Correção de Erro
    nivel_correcao = st.selectbox(
        "Nível de Correção de Erro",
        options=["M (Médio - Padrão)", "H (Alto - Melhor p/ impressão)", "L (Baixo)", "Q (Quartil)"],
        index=1 # Padrão H
    )

# Mapeamento da seleção para as constantes do qrcode
mapa_erro = {
    "L (Baixo)": qrcode.constants.ERROR_CORRECT_L,
    "M (Médio - Padrão)": qrcode.constants.ERROR_CORRECT_M,
    "Q (Quartil)": qrcode.constants.ERROR_CORRECT_Q,
    "H (Alto - Melhor p/ impressão)": qrcode.constants.ERROR_CORRECT_H,
}

# --- Área Principal ---
url = st.text_input("🔗 Cole o seu Link aqui:", placeholder="https://www.exemplo.com.br")

if url:
    # Gerando o QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=mapa_erro[nivel_correcao],
        box_size=tamanho,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # --- Convertendo para Bytes (para o Streamlit ler) ---
    # Em vez de salvar no disco, salvamos num buffer de memória
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()

    # Exibindo a imagem
    st.markdown("### Resultado:")
    st.image(img_bytes, caption=f"QR Code gerado para: {url}", use_column_width=False)

    # Botão de Download
    st.download_button(
        label="📥 Baixar QR Code (PNG)",
        data=img_bytes,
        file_name="qrcode_hd.png",
        mime="image/png"
    )
else:
    st.info("👆 Digite um link acima para gerar o código.")