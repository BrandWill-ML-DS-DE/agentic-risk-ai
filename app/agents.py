from langchain_community.chat_models import ChatOllama
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from app.explainability import generate_explanation

llm = ChatOllama(model="llama3")

def explanation_tool(transaction):
    explanation = generate_explanation(transaction)
    return str(explanation)

tools = [
    Tool(
        name="FraudExplanation",
        func=explanation_tool,
        description="Generate SHAP explanation for fraud prediction"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_investigation(transaction):
    prompt = f"""
    Investigate this financial transaction:
    {transaction}

    Determine:
    1. Fraud risk
    2. Risk factors
    3. Recommendation
    """

    return agent.run(prompt)