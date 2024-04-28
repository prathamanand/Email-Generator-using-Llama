import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get the response back
def getLLMResponse(from_input,email_sender,email_recipient,email_style):
    llm = CTransformers(model='llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})
    #Template for building the Prompt
    template = """
    Write a email with {style} style and includes topic : {email_topic}.\n\nSender: {sender}\nRecipient: {recipient}
    \n\nEmail Text:
    """

    # Creating a final PROMPT
    prompt = PromptTemplate(
        input_variables=["style", "email_topic", "sender", "recipient"],
        template=template,)

    #Getting the response using LLM
    response=llm(prompt.format(email_topic=from_input, sender=email_sender, recipient=email_recipient, style=email_style))
    print(response)

    return response



st.set_page_config(page_title="Generate Emails",
                   page_icon='📧',
                   layout='centered',
                   initial_sidebar_state='collapsed')
st.header("Generate Emails 📧")

from_input = st.text_area('Enter the email topic', height=275)

#Creating columns for the UI- To receive inputs from the user
col1, col2, col3 = st.columns([10, 10, 5])
with col1:
    email_sender = st.text_input("Sender Name")
with col2:
    email_recipient = st.text_input("Recipient Name")
with col3:
    email_style = st.selectbox('Wrting Style',
                                    ('Formal', 'Appreciating', 'Not Satisfied', 'Nuetral'),
                                        index=0)  
    
submit = st.button("Generate")

# when 'Generate' button is clicked, execute the below code
if submit:
    st.write( getLLMResponse(from_input,email_sender,email_recipient,email_style))

