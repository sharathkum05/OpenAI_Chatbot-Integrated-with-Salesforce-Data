from openai import OpenAI

import constants

client = OpenAI(
    api_key= constants.APIKEY
)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "hi, how are you?"},
                #{
                #    "type": "image_url",
                #    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                #},
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])
