import discord
import csv

keyfile = open("key.btk")
token = keyfile.read()
keyfile.close()


class Bot(discord.Client):
    async def on_ready(self):
        print('Logged in as {0}'.format(self.user))

    async def on_message(self, message):
        # !users: Gathers the names of all users on the server and prints them to a CSV file
        if "!users" in message.content.lower():
            await message.channel.send("Getting user list...")
            users = self.get_all_members()

            with open('log.csv', 'w') as output:
                writer = csv.writer(output)
                writer.writerow(['Name'])
                for user in users:
                    writer.writerow([user.display_name])


client = Bot()
client.run(token)
