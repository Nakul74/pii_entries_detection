# PII detection web app using streamlit

This is a PII (personally identifiable information) detection and validation app using Streamlit.

## Overview

🤖 This web application utilizes Streamlit, Langchain, and OpenAI.

## Prerequisites

1. Python 3.10
2. Streamlit
3. Langchain
4. OpenAI key

## Setup
1. Clone the repository:

    ```bash
    git clone https://github.com/Nakul74/pii_entries_detection.git
    ```

2. Create a Conda environment with the specified version of Python from the `runtime.txt` file:

    ```bash
    conda create -p ./envs $(cat runtime.txt) -y
    ```

3. Activate the environment:

    ```bash
    conda activate envs/
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Use the following command to run the application:

```bash
streamlit run app.py
```
