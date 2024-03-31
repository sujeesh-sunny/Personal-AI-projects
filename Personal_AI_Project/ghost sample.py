import openai

# OpenAI API key
api_key = ""

# Initialize the OpenAI API client
openai.api_key = api_key

# Contextual knowledge about the user
user_info = {
    "name": "Lucifer",
    "location": "Hell"
}


def create_ghost_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are your personal AI assistant named Ghost."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]


# Main loop for interaction
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Ghost: Of course, feel free to return whenever you need assistance.")
        break

    prompt = user_input

    # Using contextual information and keywords
    if "name" in user_info and user_info["name"].lower() in user_input.lower():
        prompt += f" My apologies, {user_info['name']}."
    # Making responses more human-like
    if "how are you" in user_input.lower():
        prompt += " I'm here and ready to help you with anything you need."
    elif "location" in user_input.lower():
        prompt += " I'm virtually everywhere, assisting users like you."
    elif "analyze" in user_input.lower():
        prompt += " I'm happy to assist you in analyzing any information you have."
    else:
        prompt += f" How can I be of service, {user_info['name']}?"

    response = create_ghost_response(prompt)
    print(f"Ghost: {response}")
