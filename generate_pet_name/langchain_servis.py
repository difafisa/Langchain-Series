from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools, get_all_tool_names

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

def langchain_agent():
  llm = ChatGoogleGenerativeAI(model='gemini-2.5-pro', temperature=0.5)
  tools = load_tools(['wikipedia', 'llm-math'], llm=llm)
  agent=initialize_agent(
    tools=tools, 
    llm=llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True ,
    handle_parsing_errors=True,
    max_iterations=3
    )
  result = agent.run("Cari berapa tahun harapan hidup seekor kucing, lalu kalikan angka tersebut dengan 3.")
  print (result)

if __name__ == "__main__":
  langchain_agent()