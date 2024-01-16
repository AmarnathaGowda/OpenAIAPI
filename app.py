import openai 
from pprint import pprint

import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv('OPENAI_API_KEY'))

openai.api_key=os.getenv('OPENAI_API_KEY')
all_modules=openai.models.list()

pprint(list(all_modules))


# client.api_key=os.getenv('OPENAI_API_KEY')
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)