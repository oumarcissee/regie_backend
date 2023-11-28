import json
from channels.generic.websocket import AsyncWebsocketConsumer
#from .models import News  # Importez le modèle correspondant


class NewsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("news_notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("news_notifications", self.channel_name)

    async def news_created(self, event):
        
        await self.send(text_data=json.dumps({"message": event["message"]}))