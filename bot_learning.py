import argparse
import json
from pathlib import Path

from environs import Env

from dialogflow_api import create_intent


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Обучение нейросети бота'
    )
    parser.add_argument(
        '--path',
        type=Path,
        default='json/questions.json',
        help='путь к JSON-файлу с фразами для обучения нейросети',
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    env = Env()
    env.read_env()
    project_id = env('DF_PROJECT_ID')
    parsed_arguments = parse_arguments()
    if not Path.exists(parsed_arguments.path):
        print('Указанный файл не найден!')
        exit(0)

    with open(parsed_arguments.path, 'r') as file:
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
