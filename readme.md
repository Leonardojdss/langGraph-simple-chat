# LangGraph Sample Chat

Este é um projeto de exemplo que demonstra como criar um chatbot simples utilizando a biblioteca [LangGraph](https://github.com/langchain-ai/langgraph) com um modelo de linguagem da OpenAI (GPT-4.1).

## Requisitos
- Python 3.10+
- Conta e chave de API da OpenAI

## Instalação
1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   cd LangGraph-sample-chat
   ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv env
   source env/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` com sua chave de API da OpenAI:
   ```env
   OPENAI_API_KEY=sk-...
   ```

## Como usar
Execute o chatbot com:
```bash
python chatbot-structure.py
```
Digite sua mensagem e o assistente responderá. Para sair, digite `quit`, `exit` ou `q`.

## Estrutura do projeto
- `chatbot-structure.py`: Código principal do chatbot.
- `requirements.txt`: Lista de dependências do projeto.

## Exemplo de uso
```
User: Olá!
Assistant: Olá! Como posso ajudar você hoje?
```

---
