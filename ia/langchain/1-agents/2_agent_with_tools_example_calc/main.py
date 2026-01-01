from langchain_ollama import ChatOllama
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from enum import Enum
from langchain.prompts import PromptTemplate
from langchain.agents import AgentExecutor
from langchain.agents.output_parsers import ReActSingleInputOutputParser
import re


class OperationType(str, Enum):
    SUM = "sum"
    MULT = "mult"
    UNKNOWN = "unknown"

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

@tool
def detect_operation(query: str) -> str:
    """
    Detecta a operação matemática (soma ou multiplicação) na consulta do usuário.
    """
    query = query.lower()

    sum_text_options = ["soma", "adicionar", "mais", "somar", "adição", "+"]
    mult_text_options = ["multiplicação", "multiplicar", "vezes", "produto", "*"]

    for text in sum_text_options:
        if text in query:
            return OperationType.SUM
    for text in mult_text_options:
        if text in query:
            return OperationType.MULT
    return OperationType.UNKNOWN

@tool
def extract_final_answer(observation: str) -> str:
    """
    Extrai a resposta final da observação.
    """
    final_response_number = observation.strip().split()[-1]
    if final_response_number.replace('.', '', 1).isdigit():
        return final_response_number
    return "Não foi possível extrair a resposta final."


llm = ChatOllama(model="qwen2.5:3b", temperature=0)

tools = [sum, mult, detect_operation, extract_final_answer]

# Criando o agente com LangGraph
prompt = PromptTemplate.from_template(
    """Você é um agente que resolve operações matemáticas.

Ferramentas disponíveis:
{tools}

Nomes das ferramentas:
{tool_names}

Use este formato exatamente:

Thought: você pensa sobre o que fazer
Action: nome da ferramenta a usar
Action Input: {{"a": valor1, "b": valor2}}
Observation: resultado da ferramenta
... (repita até ter a resposta final)
Final Answer: a resposta final para o usuário

Pergunta: {input}

{agent_scratchpad}
"""
)

agent = create_react_agent(llm, tools)

response_sum = agent.invoke({"messages": [("user", "Qual é a soma de 15 e 27?")]})
final_answer_sum = response_sum["messages"][-1].content
number_sum = re.findall(r'\d+', final_answer_sum)[-1] if re.findall(r'\d+', final_answer_sum) else final_answer_sum
print("a soma é " + number_sum)

response_mult = agent.invoke({"messages": [("user", "Qual é o produto de 8 e 12?")]})
final_answer_mult = response_mult["messages"][-1].content
number_mult = re.findall(r'\d+', final_answer_mult)[-1] if re.findall(r'\d+', final_answer_mult) else final_answer_mult
print("o produto é " + number_mult)