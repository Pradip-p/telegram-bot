import json
from datetime import datetime
from telethon import TelegramClient, functions
import django
from pathlib import Path
import os
import sys
from asgiref.sync import sync_to_async


BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django.setup()

from bot.models import BotUser, MessageContent

# #########
api_id = ""  #replace the api_id of telegram app
api_hash = "" #replace the api hash 
group_id = "" # group id of your telegram

client = TelegramClient('luke', api_id, api_hash)

@sync_to_async
def save_data_to_database(user_id, username,first_name,last_name,phone, message_content, timestamp, was_online, message_id):
    try:
        if phone and message_content:  # Check if message_content is not None or an empty string
            # Try to retrieve an existing BotUser instance by username
            bot_user = BotUser.objects.filter(user_id=user_id).first()
            
            if bot_user:
                bot_user.was_online = was_online
                bot_user.save()
                
            # If the BotUser instance doesn't exist, create a new one
            if not bot_user:
                bot_user = BotUser(user_id=user_id,username=username,first_name=first_name, last_name=last_name, phoneNumber=phone, was_online=was_online)
                bot_user.save()

            # Check if a message with the same message_id already exists
            # Try to get a message with the same message_id
            try:
                message = MessageContent.objects.get(message_id=message_id)                
            except MessageContent.DoesNotExist:
                print('save  new message of telegram members \n')
                # If it doesn't exist, create a new message
                message = MessageContent.objects.create(
                    bot_user=bot_user,
                    message_content=message_content,
                    time=timestamp,
                    message_id=message_id,
                )
            return ''
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
@sync_to_async
def save_react_time(react_user_id, react_time):
    bot_user = BotUser.objects.filter(user_id=react_user_id).first()
    if bot_user:
        # Check if recent_reaction_time is None or the new react_time is more recent
        if bot_user.recent_reaction_time is None or react_time > bot_user.recent_reaction_time:
            bot_user.recent_reaction_time = react_time
            bot_user.save()
            print('Saved the reaction time on user', react_user_id)

        
async def do_something():
    try:
        # Get participants once outside the loop
        users = await client.get_participants(group_id)
        async for message in client.iter_messages(group_id):
            user_id = message.from_id.user_id
            username = None
            react_emoji = None
            react_count = None
            msg_id = None
            #react user details
            reaction = await client(functions.messages.GetMessagesReactionsRequest(group_id, id=[message.id]))
            if reaction.updates:
                reaction = reaction.updates[0].to_dict()
                # msg_id = reaction['msg_id']
                # count = reaction['reactions']['results'][0]['count']
                recent_reactions = reaction['reactions']['recent_reactions']
                
                for recent_reaction in recent_reactions:
                    react_user_id = recent_reaction['peer_id'].get('user_id')
                    # users =  await client.get_participants(group_id)
                    react_date = recent_reaction['date']
                    # react_emoji = recent_reaction['reaction']['emoticon']
                    
                    await save_react_time(react_user_id, react_date)
            
            # Find the user with matching user_id
            for user in users:
                if user.id == user_id:
                    if user.username:
                        username = user.username
                    was_online = user.status.was_online
                    first_name = user.first_name
                    last_name = user.last_name
                    phone = user.phone
                    message_id = message.id
                    message_content = message.text
                    timestamp = datetime.fromtimestamp(message.date.timestamp())
                    
        #           Save react_emoji and react_count if available
                    # if message.id == msg_id:
                    #     react_emoji = react_emoji
                    #     react_count = react_count
                    await save_data_to_database(user_id, username, first_name, last_name, phone, message_content, timestamp, was_online, message_id)
                    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    
async def main():
    # Most of your code should go here.
    await client.start()
    await do_something()

with client:
    client.loop.run_until_complete(main())
