from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import YoutubeLoader
# from langchain_yt_dlp import YoutubeLoaderDL
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='text-embedding-001')
def create_vector_db_from_url_youtube(video_url: str) -> FAISS:
  loader = YoutubeLoaderDL.from_youtube_url(
    video_url, add_video_info=True,
  )
  transkript = loader.load()
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
  docs = text_splitter.split_documents(transkript)
  db = FAISS.from_documents(documents=docs, embedding=embedding)
  return db

if __name__ == '__main__':
  print(create_vector_db_from_url_youtube('https://www.youtube.com/watch?v=arj7oStGLkU'))