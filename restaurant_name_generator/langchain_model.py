from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = OpenAI(
    temperature = 0.6
)

name_prompt = PromptTemplate(
    input_variables = ['cuisine', 'food_type'],
    template = "I want to open a restaurant for {cuisine} food that is of {food_type} type. Suggest a fancy name for my restaurant."
)
name_chain = LLMChain(
    llm = llm,
    prompt = name_prompt,
    output_key = "restaurant_name"
)

menu_prompt = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = "Suggest some menu items for {restaurant_name}. Return it as a comma separated list."
)
menu_chain = LLMChain(
    llm = llm,
    prompt = menu_prompt,
    output_key = "menu_items"
)

def generate_restaurant_name_and_items(cuisine, food_type):
    chain = SequentialChain(
        chains = [name_chain, menu_chain],
        input_variables = ['cuisine', 'food_type'],
        output_variables = ['restaurant_name', 'menu_items']
    )
    response = chain({'cuisine': cuisine, 'food_type': food_type})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))