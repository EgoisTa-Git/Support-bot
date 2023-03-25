from environs import Env
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

env = Env()
env.read_env()
vk_token = env('VK_API_KEY')
vk_session = vk_api.VkApi(token=vk_token)

long_poll = VkLongPoll(vk_session)

for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Новое сообщение:')
        if event.to_me:
            print('Для меня от: ', event.user_id)
        else:
            print('От меня для: ', event.user_id)
        print('Текст:', event.text)
