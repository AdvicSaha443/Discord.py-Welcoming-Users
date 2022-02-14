import discord

from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
  print("Bot now online")

@bot.event
async def on_member_join(member):

  #add the channel id in which you want to send the card
  channel = bot.get_channel(884433866557915156)

  #if you want to give any specific roles to any user then you can add like this
  role = get(member.guild.roles, name="Member")
  await member.add_roles(role)

  pos = sum(m.joined_at < member.joined_at for m in member.guild.members if m.joined_at is not None)

  if pos == 1:
    te = "st"
  elif pos == 2:
    te = "nd"
  elif pos == 3:
    te = "rd"
  else: te = "th"

  background = Editor("wlcbg.jpg")
  profile_image = await load_image_async(str(member.avatar_url))

  profile = Editor(profile_image).resize((150, 150)).circle_image()
  poppins = Font.poppins(size=50, variant="bold")

  poppins_small = Font.poppins(size=20, variant="light")

  background.paste(profile, (325, 90))
  background.ellipse((325, 90), 150, 150, outline="gold", stroke_width=4)

  background.text((400, 260), f"WELCOME TO {member.guild.name}", color="white", font=poppins, align="center")
  background.text((400, 325), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")
  background.text((400, 360), f"You Are The {pos}{te} Member", color="#0BE7F5", font=poppins_small, align="center")

  file = File(fp=background.image_bytes, filename="wlcbg.jpg")

  #if you want to message more message then you can add like this
  await channel.send(f"Heya {member.mention}! Welcome To **{member.guild.name} For More Information Go To <#885152158599770183>**")

  #for sending the card
  await channel.send(file=file)

@bot.event
async def on_member_remove(member):
  channel = bot.get_channel(884433866557915156)

  await channel.send(f"{member.name} Has Left The server, We are going to miss you :( ")



bot.run("OTQyNDIxMzE2MjczODQ0Mjk2.YgkQPw.7s9_xO24t5lD4-EjKwA6i5uRFPw")