import discord
import os
import random
import time



def read_token():
	with open(r'token.txt') as f:
		lines = f.readlines()
		return lines[0].strip()
		
		
		
def get_sleep():
	global seconds
	seconds = (random.randint(2,8))

token = read_token()
client = discord.Client()
count = 1

@client.event
async def on_message(message):
    if message.content.find("and follow the") != -1:
        get_sleep()
        time.sleep(seconds)
        await message.channel.send("welcome :\)")
        os.system('cls')
        global count
        print('Greeted '+ str(count) + ' people!')
        count += 1
		
client.run(token, bot=False)