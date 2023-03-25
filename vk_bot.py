import random

from environs import Env
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType

env = Env()
env.read_env()
vk_token = env('VK_API_KEY')


def echo(event, vk_api):
    vk_api.messages.send(
        user_id=event.user_id,
        message=event.text,
        random_id=random.randint(1, 1000)
    )


if __name__ == "__main__":
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    long_poll = VkLongPoll(vk_session)
    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api)
