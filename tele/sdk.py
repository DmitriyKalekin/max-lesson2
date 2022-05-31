import requests

from config import TG_URL


async def setWebhook(whurl) -> bool:
    json_params = {
        "url": whurl,
        "allowed_updates": ["message", "edited_message", "callback_query"]
    }
    endpoint = TG_URL + "setWebhook"
    result = requests.post(endpoint, json=json_params)
    js = result.json()
    return js.get("ok", False)


async def deleteWebhook() -> bool:
    pass


async def getWebhookInfo() -> dict:
    pass


async def sendMessage(chat: int, msg: str) -> dict:
    pass
