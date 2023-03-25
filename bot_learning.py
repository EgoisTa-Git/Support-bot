import json

from environs import Env

from dialogflow_api import create_intent


if __name__ == '__main__':
    env = Env()
    env.read_env()
    project_id = env('DF_PROJECT_ID')

    with open('json/questions.json', 'r') as file:
        intents_json = file.read()
    intents = json.loads(intents_json)

    for display_name, intent in intents.items():
        training_phrases_parts = intent['questions']
        message_text = [intent['answer'], ]
        intent_status = create_intent(
            project_id,
            display_name,
            training_phrases_parts,
            message_text,
        )
        print(intent_status)
