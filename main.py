from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize language model
model = ChatGroq(model = "gemma2-9b-it", groq_api_key = groq_api_key)

# Define prompt template for translation
system_template = "Translate the following into {language} and provide only the translation"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Set up the output parser
parser = StrOutputParser()

# Create translation chain (connect prompt, model, and parser)
chain = prompt_template | model | parser

# Initialize FastAPI app
app = FastAPI(
    title="Translation API",
    version="1.0"
)

# Add API routes with Langserve
add_routes(
    app,
    chain,
    path="/chain"
)
