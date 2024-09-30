import discord
from discord.ext import commands
import os
import asyncio

sesYolu = "/home/container/merhabaoyuncu.mp3"  # DOSYA YOLUNU DEĞİŞTİR
ytRolü = 1247644798782017576   # ROL ID Sİ

async def create_bot(token, voice_channel_id):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='.', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} aktif')

        voice_channel = discord.utils.get(bot.get_guild(bot.guilds[0].id).voice_channels, id=voice_channel_id)
        if voice_channel:
            await connect_to_voice_channel(bot, voice_channel)

    async def connect_to_voice_channel(bot, voice_channel):
        if not discord.utils.get(bot.voice_clients, guild=voice_channel.guild):
            try:
                await voice_channel.connect()
                print(f'{bot.user.name} {voice_channel.name} kanalına bağlandı')
            except discord.Forbidden:
                print(f'İzin hatası: {bot.user.name} ses kanalına bağlanamıyor. Bağlanma veya konuşma izni eksik olabilir; {e} ')
            except discord.HTTPException as e:
                print(f'HTTP hatası: {str(e)}')
            except discord.ClientException as e:
                print(f'Client hatası: {str(e)}')
            except Exception as e:
                print(f'Kanal bağlanma hatası: {str(e)}')

    @bot.command()         # EĞER BOTLAR SES KANALINDAN DÜŞERSE BOTUN GİRECEĞİ SES KANALINA GİR,  BU KOMUTU KULLAN .gir
    async def gir(ctx):    
        if ctx.author.voice:
            voice_channel = ctx.author.voice.channel  
            await connect_to_voice_channel(bot, voice_channel)
            await ctx.send(f'{bot.user.name} ses kanalına katıldı!')
        else:
            await ctx.send('Öncelikle bir ses kanalına katılmalısınız.')

    @bot.event
    async def on_voice_state_update(member, before, after):
        voice_client = discord.utils.get(bot.voice_clients, guild=member.guild)

        if after.channel is not None and voice_client is not None:
            role = discord.utils.get(member.guild.roles,
            ytRolü)
            if role in member.roles and voice_client.is_playing():
                voice_client.stop()
                print(f'{bot.user.name}: {member.display_name} kanala katıldı, müzik durduruldu')

        if before.channel is None and after.channel is not None:
            if voice_client is None:
                await connect_to_voice_channel(bot, after.channel)

            if voice_client and voice_client.channel == after.channel and not any(role in m.roles for m in after.channel.members if (role := discord.utils.get(member.guild.roles,
            ytRolü))):
                await asyncio.sleep(1)  
                if not voice_client.is_playing():
                    if os.path.exists(sesYolu):
                        print(f'{sesYolu} dosyası bulunuyor!')
                        try:
                            options = "-vn -ar 48000 -ac 2 -b:a 192k -filter:a loudnorm"  # SES KALİTESİ ARTTIRICI
                            voice_client.play(discord.FFmpegPCMAudio(sesYolu, options=options))
                            print(f'{sesYolu} dosyası çalınıyor!')
                        except Exception as e:
                            print(f'Çalma hatası: {str(e)}')
                    else:
                        print(f'Hata: {sesYolu} dosyası bulunamadı')

    await bot.start(token)

async def main():
    bot_tokens = [
        "BOT_TOKEN_1", 
        "BOT_TOKEN_2", 
        "BOT_TOKEN_3"   
    ]
    voice_channel_ids = [
        1254503055517552751,   # VC CHANNEL 1 
        1254503143618772992,   # VC CHANNEL 2
        1254503169904611348    # VC CHANNEL 3
    ]

    tasks = []
    for i, token in enumerate(bot_tokens):
        tasks.append(create_bot(token, voice_channel_ids[i]))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
