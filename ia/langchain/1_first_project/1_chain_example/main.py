from langchain_ollama import ChatOllama

from langchain_core.prompts import PromptTemplate
template_string = (
    "traduza o seguinte texto para o português: {text_to_translate}"
)

#parametro a ser traduzido
text_to_translate = "hello, how are you?"

#prompt template
translation_prompt = PromptTemplate(
    input_variables=["text_to_translate"], template=template_string
)

#configuração do modelo e cadeia
llm = ChatOllama(model="qwen3-vl:4b", temperature=0)

#criação da cadeia de tradução
chain = translation_prompt | llm
formatted_prompt = translation_prompt.format(
    text_to_translate=text_to_translate)
response = chain.invoke(input={"text_to_translate": text_to_translate})
result = response.content
print(f"Prompt: {formatted_prompt}")
print(f"Response: {result}")