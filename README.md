# 🤖 Agentic AI Financial Risk Intelligence System



[![Python 3.10+](https://img.shields.io/badge/python-3.10-blue.svg)]

[![FastAPI](https://img.shields.io/badge/FastAPI-API-green)]

[![LangChain](https://img.shields.io/badge/LangChain-Agentic_AI-purple)]

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]



An **autonomous financial risk investigation agent** combining:



- Machine Learning fraud detection

- Explainable AI (SHAP)

- Agentic LLM reasoning

- Vector memory retrieval

- Real-time API deployment



The system automatically **detects suspicious financial transactions and generates human-readable investigative reports.**



---



# 🧠 System Architecture



This project combines **classical ML + Agentic AI**.



---



## 1️⃣ Fraud Detection Engine



A supervised ML model trained using **XGBoost** detects suspicious financial transactions.



### Key features



- transaction amount  

- account age  

- transaction type  

- geographic risk score  



The model outputs:



- **Fraud probability**

- **Binary classification**



---



## 2️⃣ Explainable AI Layer



Using **SHAP**, the system provides transparent explanations for predictions.



### Example output



```

Top Risk Drivers:

- Transaction Amount

- Location Risk

- Account Age

```



This ensures the system remains **auditable and compliant with financial regulations**.



---



## 3️⃣ Agentic AI Investigation System



An **LLM-powered autonomous agent** analyzes suspicious transactions and produces investigative reports.



The agent:



1. Retrieves explanations  

2. Evaluates fraud signals  

3. Produces risk recommendations  



### Built with



- LangChain

- Ollama

- LLaMA3



---



## 4️⃣ Vector Memory Store



A **FAISS vector database** stores contextual knowledge for agent reasoning.



### Capabilities



- Semantic similarity search

- Context retrieval

- AI-assisted investigation workflows



---



## Dataset



This project uses the Credit Card Fraud Detection dataset.



Download from Kaggle:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud



After downloading:



1. Extract the file

2. Rename `creditcard.csv` to `transactions.csv`

3. Place it in:



data/transactions.csv



---



# 🛠 Tech Stack



| Layer | Technology | Purpose |

|------|------|------|

| ML | XGBoost | Fraud detection |

| Explainability | SHAP | Model interpretability |

| Agents | LangChain | Autonomous investigation |

| LLM | Ollama + LLaMA3 | Local reasoning engine |

| Vector DB | FAISS | Memory retrieval |

| API | FastAPI | Production deployment |

| Tracking | MLflow | Experiment tracking |



---



# 📂 Project Structure



```

agentic-risk-ai

│

├── app

│   ├── main.py

│   ├── agents.py

│   ├── fraud_model.py

│   ├── explainability.py

│   └── vector_store.py

│

├── data

│   └── transactions.csv

│

├── requirements.txt

└── Dockerfile

```



---



# 🚀 Installation



## 1️⃣ Install dependencies



```bash

pip install -r requirements.txt

```



---



## 2️⃣ Install LLM



Install **Ollama**



https://ollama.com



Pull the model:



```bash

ollama pull llama3

```



---



## 3️⃣ Train Fraud Model



```python

from app.fraud_model import train_model



train_model()

```



---



# ▶ Run API



```bash

uvicorn app.main:app --reload

```



### Test request



```bash

curl -X POST "http://127.0.0.1:8000/analyze" 

-H "Content-Type: application/json" 

-d '{"amount":5000,"transaction_type":1,"account_age":2,"location_risk":0.8}'

```



---



# 🐳 Docker Deployment



### Build image



```bash

docker build -t agentic-risk-ai .

```



### Run container



```bash

docker run -p 8000:8000 agentic-risk-ai

```



---



# 📊 Example Response



```json

{

&nbsp; "fraud_prediction": 1,

&nbsp; "fraud_probability": 0.91,

&nbsp; "agent_report": "Transaction flagged due to unusually high amount and risky location."

}

```



---



# 🔮 Future Improvements



- Multi-agent orchestration

- Graph-based fraud detection

- Streaming transaction monitoring

- Reinforcement learning investigation agents



---



# ⚠ Disclaimer



This project is intended for **research and educational purposes only**.





