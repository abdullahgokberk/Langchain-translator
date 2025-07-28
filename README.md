# LangChain Translator

LangChain ve OpenAI GPT modeli kullanılarak geliştirilmiş bir çeviri uygulamasıdır. FastAPI ile web servisi olarak sunulmuştur.

## 🚀 Nasıl Çalıştırılır?

1. `.env` dosyasına OpenAI API ve Langchain API anahtarlarınızı ekleyin:

OPENAI_API_KEY=

LANGCHAIN_API_KEY=

2. Gerekli Python paketlerini yükleyin:

pip install -r requirements.txt
3. Uygulamayı çalıştırın:
`/chain/invoke` endpoint'ine şu formatta POST isteği gönderin:
```json
{
  "language": "italian",
  "text": "Hello"
}