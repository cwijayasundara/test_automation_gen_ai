from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

from langchain_core.messages import HumanMessage, SystemMessage

chat = ChatOpenAI(model="gpt-4-vision-preview", max_tokens=256)
response = chat.invoke(
    [
        HumanMessage(
            content=[
                {"type": "text", "text": "What is this image showing"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://raw.githubusercontent.com/langchain-ai/langchain/master/docs/static/img"
                               "/langchain_stack.png",
                        "detail": "auto",
                    },
                },
            ]
        )
    ]
)

print(response)
