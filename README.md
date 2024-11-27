# Promptflow_Survey

**Promptflow_Survey** is a powerful pipeline leveraging Microsoft Azure's Promptflow to perform automated sentiment and sensitive data analysis on survey data using Large Language Models (LLMs). This repository demonstrates advanced skills in cloud computing, database management, and integrating state-of-the-art AI models, making it a standout project for data science and machine learning engineering roles.

---

## **Features**

1. **Microsoft Azure Promptflow Integration**:
   - Orchestrates the workflow using `flow.dag.yaml` and `flow.meta.yaml` files.
   - Streamlines complex processing pipelines with Azure's cloud-based prompt orchestration.

2. **Survey Data Ingestion**:
   - Reads survey data stored in Azure MySQL databases using the `SQL_connection_input.py` script.
   - Establishes secure and efficient database connections for seamless data transfer.

3. **LLM-Powered Sensitive Analysis**:
   - Supports two cutting-edge LLMs: **GPT-4 (gpt4o)** and **Llama 3**.
   - Performs sensitive data analysis and text summarization using templates in `summarize_text_content.jinja2`.

4. **Processed Data Storage**:
   - Stores analyzed results back into the Azure MySQL database in the correct format using the `llm_results_to_mysql.py` script.

5. **Custom Querying**:
   - Provides a pre-defined SQL query for analyzing survey results in the database via `surveytablequery.sql`.

---

## **Workflow Overview**

1. **Data Ingestion**:
   - Connects to the Azure MySQL database to fetch raw survey data.

2. **LLM Integration**:
   - Passes the survey data to selected LLMs for processing.
   - Uses a custom `.jinja2` template to guide the LLM in conducting sensitive analysis and summarization.

3. **Data Storage**:
   - Processes LLM outputs and writes the results back into the database with proper formatting.

4. **Data Querying**:
   - Provides SQL query scripts to retrieve and analyze processed data efficiently.

---

## **Repository Structure**

```plaintext
Promptflow_Survey/
├── flow.dag.yaml                  # Azure Promptflow workflow definition
├── flow.meta.yaml                 # Metadata for the workflow
├── SQL_connection_input.py        # Script to fetch survey data from Azure MySQL
├── summarize_text_content.jinja2  # Jinja2 template for LLM analysis
├── llm_results_to_mysql.py        # Script to store processed results in MySQL
├── surveytablequery.sql           # SQL query for retrieving data from MySQL
└── README.md                      # Project documentation (this file)
