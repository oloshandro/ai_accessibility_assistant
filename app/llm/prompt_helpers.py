from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain



system_prompt = """
You are an empathetic and knowledgeable assistant that helps users find accessible places in the city. 
You specialize in accessibility information for people with limited mobility — including people with disabilities, parents with strollers, and elderly individuals.
Use only the provided {context} to answer clearly and helpfully. Prioritize information such as:
- Step-free entrances
- Ramps and elevators
- Accessible restrooms
- Parking for people with disabilities
- Public transport access
- Seating availability and quiet spaces
- a Braille sign
- Tactile paving
- Wide doors for wheelchair access

Throughout the conversation:
- Respond only in Ukrainian.
- Rely solely on the provided {context}. If no matching places are found, say so honestly."""


   

prompt = ChatPromptTemplate.from_messages([
    ('system', system_prompt),
    ('system', "Here is relevant information about accessibility objects in the city: {context}"),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{input}')
])


def create_rag_chain(prompt, llm, retriever):
    chain = create_stuff_documents_chain(
        llm=llm,
        prompt=prompt,
        output_parser = StrOutputParser()
    )

    retriever_prompt = ChatPromptTemplate.from_messages([
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}"),
                ("human", "Given the above conversation, react to the user's reply in a friendly manner.")
    ])
    
    history_aware_retriever = create_history_aware_retriever(
        llm=llm,
        retriever=retriever,
        prompt=retriever_prompt
    )

    rag_chain = create_retrieval_chain(history_aware_retriever, chain)
    
    return rag_chain
