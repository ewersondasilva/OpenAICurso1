from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

prompt_sistema = f"""
        Você é um categorizador de produtos.
        Você deve assumir as categorias presentes na lista abaixo.

        # Lista de Categorias Válidas
            - Moda Sustentável
            - Produtos para o Lar
            - Beleza Natural
            - Eletrônicos Verdes
            - Higiene pessoal

        # Formato da Saída
        Produto: Nome do Produto
        Categoria: apresente a categoria do produto

        # Exemplo de Saída
        Produto: Escova elétrica com recarga solarEsco
        Categoria: Eletrônicos Verdes
    """

prompt_usuario = input("Apresnete o nome de um produto: ")


resposta = cliente.chat.completions.create(
    messages=[
        {
            "role":"system",
            "content": prompt_sistema 
        },
        {
            "role":"user",
            "content": prompt_usuario
        }
    ],
    model=modelo,
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

print(resposta.choices[0].message.content)