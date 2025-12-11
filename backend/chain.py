from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from .memory import add_message, get_memory



def build_chain(vectorstore):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    memory = get_memory()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that answers based on retrieved context."),
        ("human", "{question}")
    ])

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
