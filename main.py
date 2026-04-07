import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def main():
    load_dotenv()
    llm = ChatOpenAI(model="gpt-4o-mini")
    print(llm.invoke("Xin chào?").content)

if __name__ == "__main__":
    main()