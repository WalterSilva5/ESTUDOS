from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain.callbacks.base import BaseCallbackHandler
from enum import Enum


# =====================
# CallbackHandler
# =====================
class SimpleCallback(BaseCallbackHandler):

    def on_agent_action(self, action, **kwargs):
        print(f"\n> TOOL: {action.tool}")
        print(f"> INPUT: {action.tool_input}")

    def on_tool_end(self, output, **kwargs):
        print(f"> RESULTADO: {output}")

    def on_agent_finish(self, finish, **kwargs):
        print(f"\n> RESPOSTA FINAL: {finish.return_values['output']}")


# =====================
# Enum
# =====================
class OperationType(str, Enum):
    SUM = "sum"
    MULT = "mult"
    UNKNOWN = "unknown"


# =====================
# Tools
# =====================
@tool
def sum(a: int, b: int) -> int:
    """Soma dois números"""
    return a + b


@tool
def mult(a: int, b: int) -> int:
    """Multiplica dois números"""
    return a * b


@tool
def detect_operation(query: str) -> str:
    """Detecta a operação matemática"""
    query = query.lower()

    if any(x in query for x in ["soma", "somar", "mais", "+"]):
        return OperationType.SUM
    if any(x in query for x in ["multiplicação", "multiplicar", "vezes", "*"]):
        return OperationType.MULT
    return OperationType.UNKNOWN


# =====================
# LLM
# =====================
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

tools = [sum, mult, detect_operation]


# =====================
# Prompt ReAct (obrigatório)
# =====================
prompt = PromptTemplate.from_template(
    """Você é um agente que resolve operações matemáticas.

Ferramentas disponíveis:
{tools}

Nomes das ferramentas:
{tool_names}

Use este formato:

Thought: ...
Action: ...
Action Input: ...
Observation: ...
Final Answer: ...

Pergunta: {input}

{agent_scratchpad}
"""
)


# =====================
# Agent + Executor
# =====================
agent = create_react_agent(llm, tools, prompt)

callback = SimpleCallback()

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    callbacks=[callback],
    verbose=False
)


# =====================
# Execução
# =====================
agent_executor.invoke({"input": "Qual é a soma de 15 e 27?"})
agent_executor.invoke({"input": "Qual é o produto de 8 e 12?"})
