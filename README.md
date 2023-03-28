# Support Bot

![demo_vk_bot.gif](assets/demo_vk_bot.gif)

Бот-помощник будет закрывать все типичные вопросы, а вот что-то посложнее – перенаправлять на операторов.
По предварительной оценке, это на 70% сократит время ожидания ответа и на 90% повысит довольство жизнью сотрудников службы поддержки.
Никогда не знаешь, как им придёт в голову сформулировать вопрос. Предсказать варианты заранее невозможно. Поэтому бот будет… обучаемый нейросетью!

## Пример бота
Доступен по ссылке в Телеграм: [Support Bot](https://t.me/dvmn_smart_support_bot)

![demo_tg_bot.gif](assets/demo_tg_bot.gif)

## Запуск
- Рекомендуется использовать виртуальное окружение для запуска проекта
- Для корректной работы Вам необходим Python версии 3.6 и выше
- API-ключ для работы с Telegram-ботом (инструкция [тут](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)).
- Скачайте код (`git clone`)
- Установите зависимости командой
```bash
pip install -r requirements.txt
```
- Для запуска нейросети необходимо получить `project_id` и файл-json с параметрами google_application_credentials.
- Для взаимодействия с API ВКонтакте необходимо получить ключ доступа API Вконтакте ([Работа с API](https://vk.com/dev/access_token)) с правами управление сообществом и доступ к сообщениям сообщества
- Перед первым запуском необходимо обучить нейросеть
```bash
python bot_learning.py
```
- Файл с обучающими фразами можно посмотреть - <a href="./json/questions.json">тут</a>.
- Для запуска Telegram-бота необходимо выполнить команду:
```bash
python tg_bot.py
```

Для запуска VK-бота необходимо выполнить команду:
```bash
python3 vk_bot.py
```

### DialogFlow

- Для получения `project_id` необходимо создать проект [DialogFlow](https://cloud.google.com/dialogflow/es/docs/quick/setup).
- Необходимо создать [агента DialogFlow](https://cloud.google.com/dialogflow/es/docs/quick/build-agent).
- Для получения файла-json с параметрами google_application_credentials необходимо:
  - установить [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
  - выполнить [авторизацию](https://cloud.google.com/docs/authentication/provide-credentials-adc) c использованием Google Cloud CLI


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, 
создайте файл `.env` в корневой директории проекта и запишите туда данные в таком 
формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:

- `TG_BOT_APIKEY` - Ваш API-ключ для работы с Telegram-ботом
- `DF_PROJECT_ID` - Ваш ID проекта DialogFlow
- `VK_API_KEY` - Ваш API-ключ для работы с VK-ботом

## Аргументы

Для настройки обучения нейросети бота используйте:

**Необязательные аргументы**
```shell
  --path JSON   путь к JSON-файлу с фразами для обучения нейросети
```
**Например:**
```shell
python bot_learning.py --path json/questions.json
```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).