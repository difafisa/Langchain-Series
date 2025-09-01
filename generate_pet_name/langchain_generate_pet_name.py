from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(makhluk_hidup, warna, sifat ):
  llm = ChatGoogleGenerativeAI(model='gemini-2.5-pro',  temperature=0.7)
  prompt = ChatPromptTemplate.from_messages(
    [
      ("system", "Kamu adalah ahli filosofi dan ahli dalam memberikan nama berdasarkan sifat-sifat {makhluk_hidup}"),
      ("human", "aku ingin nama {makhluk_hidup} yang keren bernuansa Indonesia, berwarna {warna} bersifat {sifat}. Buat nama tersebut masih mengandung unsur {makhluk_hidup} didalamnya, rekomendasikan 5 nama keren")
    ]
  )
  # Tambahan: Output parser untuk mendapatkan hasil dalam bentuk string bersih
  output_parser = StrOutputParser()
  chain = prompt | llm | output_parser
  response = chain.invoke(
    {
      "makhluk_hidup" : makhluk_hidup,
      "warna" : warna,
      "sifat" : sifat 
    }
  )
  return response

# def generate_pet_name():
#   llm = ChatGoogleGenerativeAI(model='gemini-2.5-pro',  temperature=0.7)
#   prompt = "Aku punya kucing dan aku ingin nama yang keren bernuansa Indonesia, rekomendasikan 5 nama keren untuk kucing ku, buat hanya berisi list nama saja"
#   name = llm.invoke(prompt)
#   return name 

