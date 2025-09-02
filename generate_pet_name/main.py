import langchain_servis as lgpn
import streamlit as st

st.title("Buat Nama Peliharaanmu")
animal_type = st.sidebar.selectbox("Apa jenis peliharaanmu ?", ("Kucing", "Anjing", "Hamster", "Sapi", "Ikan"))
label = {
  "Kucing" : "Apa warna kucing mu?",
  "Anjing" : "Apa warna anjing mu?",
  "Hamster" : "Apa warna hamster mu?",
  "Sapi" : "Apa warna sapi mu?",
  "Ikan" : "Apa warna Ikan mu?"
}

pet_color = st.sidebar.text_area(
  label = label[animal_type],
  max_chars=25
)

pet_characteristic = st.sidebar.text_area(
  label="Apa sifat unik peliharaanmu?",
  max_chars=25
)

if st.sidebar.button("Buat"):
  if not pet_color or not pet_characteristic:
    st.info("isi warna atau sifat peliharaanmu")
    st.stop()
  response = lgpn.generate_pet_name(animal_type, pet_color, pet_characteristic)
  st.text(response)

