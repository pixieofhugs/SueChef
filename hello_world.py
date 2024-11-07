
from openai import OpenAI
import os

# Load the API key from the environment variable
api_key = os.getenv("SUE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please check your environment variable.")


