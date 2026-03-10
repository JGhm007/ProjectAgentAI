import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

class PlanningAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3-flash-preview", # Gemini 3 model
            temperature=0.3
        )
        # Prompt
    def plan_tasks(self, tasks):
        prompt = ChatPromptTemplate.from_template("""
        You are an expert planning assistant.
        Organize these tasks: {task_list}
        Prioritize by urgency and create a table.
        """)
        
        # We use the capitalized class
        chain = prompt | self.llm | StrOutputParser()
        
        try:
            return chain.invoke({"task_list": str(tasks)})
        except Exception as e:
            return f" Error: {e}"