# ICBF Bilingual ChatBot (Unofficial)
A bilingual ChatBot created to answer to FAQs asked to the Colombian Institute for Family Welfare (ICBF).

The application was carried out by performing webscraping of the [Frequent Answers to Questions](https://www.icbf.gov.co/servicios/preguntas-y-respuestas-frecuentes) of the ICBF. Then, the answers were preprocessed and stored in a FAISS vector store. A LLMChain that uses GPT-3.5 is then used to process incoming user questions to look for accurate responses in the Vector Store. The deployed chain is hosted in Databricks, and the Frontend is hosted as a Streamlit App.

This worked is based on the [QA Bot Databricks Industry Solutions Accelerator](https://github.com/databricks-industry-solutions/diy-llm-qa-bot) and the Frontend Source Code is based on the code samples provided in the [Streamlit Documentation site for Conversational Apps](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps).

#### This repository serves as the source of the Streamlit Frontend of the application
