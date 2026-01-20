from model.intents import intents, responses


def get_intent(user_input):
    user_input = user_input.lower()

    for intent, keywords in intents.items():
        for word in keywords:
            if word in user_input:
                return intent

    return "default"

def get_response(user_input):
    intent = get_intent(user_input)
    return responses.get(intent, responses["default"])
