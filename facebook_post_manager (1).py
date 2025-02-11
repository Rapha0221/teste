try:
    import streamlit as st
    import pandas as pd
except ModuleNotFoundError:
    st.error("Erro: A biblioteca 'streamlit' não está instalada. Instale-a com 'pip install streamlit'.")
    import sys
    sys.exit()

# Nome do arquivo da planilha
FILE_NAME = "postagens_facebook.xlsx"

def load_data():
    """Carrega a planilha se existir, senão cria um DataFrame vazio."""
    try:
        return pd.read_excel(FILE_NAME)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Título", "Link", "Data de Postagem", "Reprogramado", "Reels"])

def save_data(df):
    """Salva os dados na planilha."""
    df.to_excel(FILE_NAME, index=False)

# Carregar dados existentes
df = load_data()

# Interface Streamlit
st.title("Gerenciador de Postagens do Facebook")

# Formulário para adicionar postagens
with st.form("add_post_form"):
    titulo = st.text_input("Título do Vídeo")
    link = st.text_input("Link do Vídeo")
    data_postagem = st.date_input("Data de Postagem")
    reprogramado = st.checkbox("Reprogramado")
    reels = st.checkbox("Reels")
    submit_button = st.form_submit_button("Adicionar Vídeo")

    if submit_button:
        novo_video = pd.DataFrame({
            "Título": [titulo],
            "Link": [link],
            "Data de Postagem": [data_postagem],
            "Reprogramado": ["Sim" if reprogramado else "Não"],
            "Reels": ["Sim" if reels else "Não"]
        })
        df = pd.concat([df, novo_video], ignore_index=True)
        save_data(df)
        st.success("Vídeo adicionado com sucesso!")

# Mostrar tabela com postagens
st.subheader("Postagens Salvas")
st.dataframe(df)

# Botão para baixar planilha
st.download_button(
    label="Baixar Planilha",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name="postagens_facebook.csv",
    mime='text/csv'
)