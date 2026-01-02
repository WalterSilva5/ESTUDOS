from langchain_ollama import ChatOllama
from langchain.tools import tool

@tool
def sum(a: int, b: int) -> int:
    """Sum two integers."""
    return a + b

llm = ChatOllama(model="qwen2.5:3b")
llm_with_tools = llm.bind_tools([sum])

response = llm_with_tools.invoke("Qual é a soma de 10 e 20?")

if response.tool_calls:
    for tool_call in response.tool_calls:
        tool_name = tool_call['name']
        tool_args = tool_call['args']
        
        if tool_name == 'sum':
            result = sum.invoke(tool_args)
            print(f"Ferramenta '{tool_name}' executada com argumentos {tool_args}")
            print(f"Resultado: {result}")
else:
    print("Nenhuma ferramenta foi chamada")
    print(f"Resposta do modelo: {response.content}")