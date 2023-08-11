# Importing required libraries
import json
import requests
import pandas as pd
import streamlit as st

# Constants
ENDPOINT_URL = "https://factored-training.cloud.databricks.com/serving-endpoints/icbf_llm-qabot-endpoint/invocations"


# Functions
def prompt_to_dataset(prompt):
    return pd.DataFrame({"question": [prompt]})


def create_tf_serving_json(data):
    return {
        "inputs": {name: data[name].tolist() for name in data.keys()}
        if isinstance(data, dict)
        else data.tolist()
    }


def score_model(dataset, url):
    headers = {
        "Authorization": f'Bearer {st.secrets["DATABRICKS_API_TOKEN"]}',
        "Content-Type": "application/json",
    }
    ds_dict = (
        {"dataframe_split": dataset.to_dict(orient="split")}
        if isinstance(dataset, pd.DataFrame)
        else create_tf_serving_json(dataset)
    )
    data_json = json.dumps(ds_dict, allow_nan=True)
    response = requests.request(
        method="POST", headers=headers, url=url, data=data_json
    )
    if response.status_code != 200:
        raise Exception(
            f"Request failed with status {response.status_code}, {response.text}"
        )

    return response.json()


def formatting_response_text(response):
    text = f"""{response['predictions'][0]['answer']}
    __Más información / More info:__ {response['predictions'][0]['source']}"""
    return text


def overall_method(prompt):
    dataset = prompt_to_dataset(prompt)
    raw_response = score_model(dataset, ENDPOINT_URL)
    final_response = formatting_response_text(raw_response)
    return final_response
