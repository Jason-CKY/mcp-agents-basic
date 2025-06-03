import os
from dotenv import load_dotenv
from smolagents import CodeAgent, WebSearchTool, OpenAIServerModel

load_dotenv()

model = OpenAIServerModel(
    model_id="deepseek/deepseek-chat-v3-0324:free",
    api_base="https://openrouter.ai/api/v1", # Leave this blank to query OpenAI servers.
    api_key=os.environ["OPENAI_API_KEY"]
)
agent = CodeAgent(tools=[WebSearchTool()], model=model, stream_outputs=True)

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")