from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field

from langchain_core.output_parsers import PydanticOutputParser

# Simple prompt without JSON formatting

class OutputTemplate(BaseModel):
    translation: str = Field(..., description="The translated text in Portuguese.")

print("Configurando o parser de saída...")
parser = PydanticOutputParser(pydantic_object=OutputTemplate)
print(f"exemplo de saída esperada: {parser.get_format_instructions()}")
llm = ChatOllama(
    model="qwen2.5:3b", 
    temperature=0,
    top_p=0.9,
    top_k=40,
    num_predict=100,
)

prompt = f"traduza para português: hello, how are you? expected output format: {parser.get_format_instructions()}"
print("Executando...")
response = llm.invoke(prompt)
print(f"RESPONSE:\n{response.content}")