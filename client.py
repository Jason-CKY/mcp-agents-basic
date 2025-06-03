import os
from dotenv import load_dotenv
import gradio as gr

from mcp.client.stdio import StdioServerParameters
from smolagents import InferenceClientModel, CodeAgent, ToolCollection, OpenAIServerModel
from smolagents.mcp_client import MCPClient

load_dotenv()

try:
    mcp_client = MCPClient(
        ## Try this working example on the hub:
        # {"url": "https://abidlabs-mcp-tools.hf.space/gradio_api/mcp/sse"}
        {"url": "http://localhost:8000/sse", "transport": "sse"}
    )
    tools = mcp_client.get_tools()

    model = OpenAIServerModel(
    model_id="deepseek/deepseek-chat-v3-0324:free",
    api_base="https://openrouter.ai/api/v1", # Leave this blank to query OpenAI servers.
    api_key=os.environ["OPENAI_API_KEY"]
    )
    agent = CodeAgent(tools=[*tools], model=model)

    demo = gr.ChatInterface(
        fn=lambda message, history: str(agent.run(message)),
        type="messages",
        examples=["What is the weather in Singapore?", "What is the prime factors of 58?", "analyze sentiment of this sentence: this product is great!"],
        title="Agent with MCP Tools",
        description="This is a simple agent that uses MCP tools to answer questions.",
    )

    demo.launch()
finally:
    mcp_client.disconnect()

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(messages=[], stream=False)
