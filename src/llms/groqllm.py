from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

class GroqLLM:
    """
    A wrapper class to load and return the Groq LLM from environment.
    """

    def __init__(self):
        load_dotenv()

    def get_llm(self):
        """
        Returns a ChatGroq LLM instance.
        """
        try:
            self.groq_api_key = os.getenv("GROQ_API_KEY")
            if not self.groq_api_key:
                raise ValueError("GROQ_API_KEY not found in environment variables")

            llm = ChatGroq(
                api_key=self.groq_api_key,
                model="gemma2-9b-it"
            )
            return llm
        
        except Exception as e:
            raise ValueError(f"Error occurred: {e}")
