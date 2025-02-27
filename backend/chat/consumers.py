from channels.generic.websocket import AsyncWebsocketConsumer

class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('TESTING FOR CONNECTION AND REDIS')
        await self.accept()