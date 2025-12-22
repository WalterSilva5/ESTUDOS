from langchain.agents import initialize_agent, AgentType
from langchain_ollama import ChatOllama
from langchain.tools import tool

# Usando o decorator @tool para registrar a função 'somar' como uma ferramenta
@tool
def somar(a: int, b: int) -> int:
    """
    Soma dois números e retorna o resultado.
    """
    return a + b

llm = ChatOllama(model="qwen3-vl:4b", temperature=0)

tools = [somar]

agent = initialize_agent(
    tools,
    llm,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# Perguntando ao agente
response = agent.invoke({"input": "Qual é a soma de 2 e 3?"})

# Exibindo a resposta
print("Response:", response["output"])
