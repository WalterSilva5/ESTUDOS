from langchain.agents import initialize_agent, AgentType
from langchain_ollama import ChatOllama
from langchain.tools import tool

@tool
def somar(numeros: str) -> int:
    """
    Soma dois números separados por vírgula e retorna o resultado.
    Entrada: 'a,b' onde a e b são números inteiros.
    Exemplo: '2,3' retorna 5
    """
    # Remove quotes if present
    numeros = numeros.strip().strip("'\"")
    parts = numeros.split(',')
    if len(parts) != 2:
        return f"Erro: esperado 2 números separados por vírgula, recebi: {numeros}"
    try:
        a, b = map(int, parts)
        return a + b
    except ValueError as e:
        return f"Erro ao converter para inteiros: {e}"

llm = ChatOllama(model="qwen3-vl:4b", temperature=0)

tools = [somar]

agent = initialize_agent(
    tools,
    llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Perguntando ao agente
response = agent.invoke({"input": "Qual é a soma de 2 e 3?"})

# Exibindo a resposta
print("Response:", response["output"])