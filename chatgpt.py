import openai
import GPT_Cay
openai.api_key = openai.api_key

openai.ChatCompletion.create(
  model="gpt-3.5-turbo"
  ,
  messages=[
        {"role": "system", "content": "You are a helpful assistant."}
           ]

)