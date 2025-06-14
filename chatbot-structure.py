from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages


class State(TypedDict):
    # As mensagens têm o tipo "list". A função `add_messages` 
    # na anotação define como essa chave de estado deve ser atualizada
    # (neste caso, ela adiciona mensagens à lista, em vez de sobrescrevê-las)
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model("openai:gpt-4.1")

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# O primeiro argumento é o nome único do nó
# O segundo argumento é a função ou objeto que será chamado sempre que
# o nó for utilizado.
graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")

graph = graph_builder.compile()

from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    pass

def stream_graph_updates(messages: list):
    for event in graph.stream({"messages": messages}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)
            result = {"assistant-response": value["messages"][-1].content}
            return result

memory = []

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        # Adiciona a mensagem do usuário ao histórico
        memory.append({"role": "user", "content": user_input})
        # Passa o histórico completo para o fluxo
        chat = stream_graph_updates(memory)
        # Adiciona a resposta do assistente ao histórico
        memory.append({"role": "assistant", "content": chat["assistant-response"]})
    except Exception as e:
        print("Erro:", e)
        break