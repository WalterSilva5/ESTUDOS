from langchain_ollama import ChatOllama
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent

# Usando o decorator @tool para registrar funções como ferramentas
@tool
def sum(a: int, b: int) -> int:
    """
    Soma dois números e retorna o resultado.
    """
    return a + b

@tool
def mult(a: int, b: int) -> int:
    """
    Multiplica dois números e retorna o resultado.
    """
    return a * b

llm = ChatOllama(model="qwen2.5:3b", temperature=0)

tools = [sum, mult]

# Criando o agente com LangGraph
agent = create_react_agent(llm, tools)

# Perguntando ao agente
print("calculating sum...")
response_sum = agent.invoke({"messages": [{"role": "user", "content": "Qual é a soma de 2 e 3?"}]})
print("Response sum:", response_sum["messages"][-1].content)

print("\ncalculating multiplication...")
response_mult = agent.invoke({"messages": [{"role": "user", "content": "Qual é o produto de 4 e 5?"}]})
print("\n\n\nResponse mult:", response_mult["messages"][-1].content)