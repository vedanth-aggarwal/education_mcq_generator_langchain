import streamlit as st
import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import OpenAI
#from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.callbacks import get_openai_callback
import PyPDF2
from langchain.chains import SequentialChain
import sys
from src.mcqgenerator.utils import read_file,get_table_data
from src.mcqgenerator.logger import logging
from src.mcqgenerator.MCQGenerator import gen_eval_chain

with open("C:\\Users\\vedan\\OneDrive\\Desktop\\mcqgen\\response.json",'r') as file:
    RESPONSE_JSON = json.load(file)

st.title('MCQ GENERATOR')

with st.form('user_inputs'):
    uploaded_file = st.file_uploader('Uplaod PDF')
    mcq_count = st.number_input('No of MCQ',min_value=3,max_value=50)
    subject = st.text_input('Subject',max_chars=30)
    tone = st.text_input('Difficulty Level',max_chars=20,placeholder='Simple')
    button = st.form_submit_button('Create MCQ')

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner('loading...'):
            try:
                text = read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response=gen_eval_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject":subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        })
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error(f'Error!{e}')
            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response,dict):
                    quiz = response.get('quiz',None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            print(table_data)
                            df = pd.DataFrame(table_data)
                            df.index+=1
                            st.table(df)
                            st.text_area(label='Review',value=response['review'])
                        else:
                            st.error('Error in table data!')
                else:
                    st.write(response)



