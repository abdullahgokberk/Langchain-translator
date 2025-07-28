from dotenv import load_dotenv, dotenv_values
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
#Output'un hangi formatta vs gelmesini istediğimizi parse eden (düzenleyen) kütüphane.
from langchain_core.output_parsers import StrOutputParser
#Konuşmayı dinamik hale getirmek için gerekli
from langchain_core.prompts import ChatPromptTemplate
#Deploy etmek için gerekli alttaki kütüphaneler. FastApi hızlı ve basit webuygulaması yapmamızı sağlayan frameworktür (Django ve Flask gibi).
from fastapi import FastAPI
#/chain/invoke URL'sine POST isteği atıldığında zinciri tetikler.
#FastAPI uygulaması ile zinciri dış dünyaya açar
#Local'de arayüz oluşturur. Tüm zinciri görebiliriz.
from langserve import add_routes
import uvicorn

load_dotenv()
#print(dotenv_values(".env").get("OPENAI_API_KEY"))
model= ChatOpenAI(model ="gpt-3.5-turbo"
                  ,temperature=0.1)
#Aşağıda normal bi istek gönderimi mevcut, en basit hali.
#messages = [
#    SystemMessage(content="Translate the following from Turkish to English"),
#    HumanMessage(content="Selam"),
#]print(chain.invoke(messages))

system_prompt = "Translate the following to {language}"
#Süslü parantezli kısımlar dinamik hale geldi. Chain'in en başına ekliyoruz ki sözlük yapısındaki dinamik textleri modele gönderilecek prompt hale soksun.
#(Basitçe dinamik yapıyı yukardaki message haline getiriyor.)
prompt_template = ChatPromptTemplate.from_messages([
    ("system",system_prompt), ("user","{text}")
])

parser = StrOutputParser()
#modelin çıktılarını bağlamak için | kullanırız
chain = prompt_template | model | parser

app = FastAPI(
    title="Translator App"
    ,version="1.0.0"
)

add_routes(
    app
    ,chain
    ,path="/chain")

print(chain.invoke({"language":"italian","text": "Hi"}))
uvicorn.run(app, host="localhost", port=8000)