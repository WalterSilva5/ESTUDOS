from langchain.agents import initialize_agent, AgentType
from langchain_ollama import ChatOllama
from langchain.tools import Tool
from langchain.callbacks.base import BaseCallbackHandler


class StopAfterObservation(BaseCallbackHandler):
    def __init__(self):
        self.stop = False

    def on_tool_end(self, output, **kwargs):
        print("🔹 Forçando parada após Observation.")
        self.stop = True
        self.result = output
        raise KeyboardInterrupt
    
def somar(a, b):
    return a + b


tools = [
    Tool(
        name="Calculadora",
        func=lambda q: somar(2, 3),
        description="Soma dois números e retorna o resultado."
    )
]


llm = ChatOllama(model="qwen3-vl:4b", temperature=0)

agent = initialize_agent(
    tools,
    llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

handler = StopAfterObservation()

try:
    response = agent.invoke(
        {"input": "Qual é a soma de 2 e 3?"},
        config={"callbacks": [handler]}
    )
    print("Response:", response["output"])
except KeyboardInterrupt:
    if hasattr(handler, "result"):
        print(f"Resultado da soma: {handler.result}")
