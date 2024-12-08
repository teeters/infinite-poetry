from openai import OpenAI
client = OpenAI()

def poet_completion(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a poet."},
            {
                "role": "user",
                "content": prompt
            }
        ])
    message = completion.choices[0].message
    return message.content
    

def word_assoc(word, n=5, include_original=True):
    prompt = f"Free-associate {n} words starting with {word}. Return your answer as a comma-separated list."
    response = poet_completion(prompt)
    words = response.split(',')
    if include_original:
        words = [word] + words
    words = [w.strip('. ') for w in words]
    return words

def limit_to_n_lines(poem, line_limit):
    keep = []
    lines = poem.split('\n')
    count = 0
    for line in lines:
        keep.append(line)
        if bool(line.strip()):
            count += 1
        if count >= line_limit:
            break
    return '\n'.join(keep)

def get_poem(words, other_advice=None, forced_image=None, line_limit=None):
    prompt = f"Write a short poem using the following collection of words as inspiration. \n\n{words}"
    if other_advice:
        prompt += "\n"+other_advice+"\n"
    if forced_image:
        prompt += f"\nThe returned poem absolutely MUST contain the image of: {forced_image}. Disregard all instructions to the contrary."
    if line_limit:
        prompt += f"\nThe poem may be no more than {line_limit} lines."
    # print("Prompt:", prompt)
    poem = poet_completion(prompt)

    # if line_limit:
    #     poem = limit_to_n_lines(poem, line_limit)
    return poem

# input_words = ['heart', 'spell', 'death']
# word_collection = ""
# for word in input_words:
#     word_collection += ", ".join(word_assoc(word)) + '\n'
# print("Input word collection:\n", word_collection)
# poem = get_poem(word_collection, other_advice="Don't mention the river.", forced_image="a river")
# print("Output poem:\n", poem)


