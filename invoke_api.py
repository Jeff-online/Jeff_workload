# import os 
# from azure.ai.inference import ChatCompletionsClient
# from azure.ai.inference.models import SystemMessage,UserMessage
# from azure.core.credentials import AzureKeyCredential

# endpoint = os.getenv("AZURE_INFERENCE_SDK_ENDPOINT","https://az102hub7108355494.services.ai.azure.com/models")
# model_name=os.getenv("DEPLOYMENT_NAME","Phi-4")
# key=os.getenv("AZURE_INFERENCE_SDK_KEY","3uoar3znC6zXRLmY5omE2trfhmkMwpfkTG9Xi6tQv9Aq8gMSm6poJQQJ99BEACYeBjFXJ3w3AAAAACOGUM7D")
# client = ChatCompletionsClient(endpoint=endpoint,credential=AzureKeyCredential(key))
# response = client.complete(messages=[
#     SystemMessage(content="You are a helpful assistant"),
#     UserMessage(content="What are 3 things to visit in Seattle?")
# ],
# model=model_name,
# max_tokens=1000
# )
# print(response)


import os 
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage,UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = os.getenv("AZURE_INFERENCE_SDK_ENDPOINT","https://az102hub7108355494.services.ai.azure.com/models")
model_name=os.getenv("DEPLOYMENT_NAME","GPT-4o")
key=os.getenv("AZURE_INFERENCE_SDK_KEY","3uoar3znC6zXRLmY5omE2trfhmkMwpfkTG9Xi6tQv9Aq8gMSm6poJQQJ99BEACYeBjFXJ3w3AAAAACOGUM7D")
client = ChatCompletionsClient(endpoint=endpoint,credential=AzureKeyCredential(key))
response = client.complete(messages=[
    SystemMessage(content="You are a helpful assistant"),
    UserMessage(content="What are 3 things to visit in Seattle?")
],
model=model_name,
max_tokens=1000
)
print(response['choices'][0]['message']['content'])



