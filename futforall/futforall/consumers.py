import json
from channels.generic.websocket import AsyncWebsocketConsumer
from notifc.models import Notification
from asgiref.sync import sync_to_async

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'notifications',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'notifications',
            self.channel_name
        )

    async def receive(self, text_data):
        print("하예솔", self.channel_name)
        if not text_data:
            return

        try:
            data = json.loads(text_data)
            message = data['message']
            user_id = data['user_id']
            timestamp = data['timestamp']
        except (KeyError, json.JSONDecodeError) as e:
            print('Error:', str(e))
            return

        await self.channel_layer.group_send(
            'notifications',
            {
                'type': 'notification_message',
                'message': message,
                'timestamp': timestamp,
            }
        )

    async def notification_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def match_join(self, event):
        await self.send(text_data=json.dumps(event))

    async def match_leave(self, event):
        await self.send(text_data=json.dumps(event))