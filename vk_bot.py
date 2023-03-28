import random

from environs import Env
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType

from dialogflow_api import detect_intent_texts

env = Env()
env.read_env()
vk_token = env('VK_API_KEY')


def reply_on_message(event, vk_api):
    project_id = env('DF_PROJECT_ID')
    text = event.text
    session_id = event.user_id
    response_text = detect_intent_texts(project_id, session_id, text)
    if response_text:
        vk_api.messages.send(
            user_id=event.user_id,
            message=response_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    long_poll = VkLongPoll(vk_session)
    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reply_on_message(event, vk_api)
