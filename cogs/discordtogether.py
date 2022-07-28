import discord, asyncio, datetime
from discord.ext import commands

try:
    from discord_together import DiscordTogether

except:
    __import__("os").system("pip install discord-together")
    from discord_together import DiscordTogether

class discordtogether(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.togetherControl = await DiscordTogether(self.bot.http.token) 

    @commands.command(aliases=['youtube'])
    @commands.cooldown(2, 10, commands.BucketType.user)
    async def youtubetogether(self, ctx):
        try:
            link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        except:
            return await ctx.send("Error! Please join a voice channel.")

        embed=discord.Embed(
            title="Youtube Together", 
            description=f"[Click Here]({link})", 
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['poker'])
    @commands.cooldown(2, 10, commands.BucketType.user)
    async def pokertogether(self, ctx):
        try:
            link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
        except:
            return await ctx.send("Error! Please join a voice channel.")

        embed=discord.Embed(
            title="Poker Together", 
            description=f"[Click Here]({link})", 
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['chess'])
    @commands.cooldown(2, 10, commands.BucketType.user)
    async def chesstogether(self, ctx):
        try:
            link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
        except:
            return await ctx.send("Error! Please join a voice channel.")

        embed=discord.Embed(
            title="Chess Together", 
            description=f"[Click Here]({link})", 
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['betrayal'])
    @commands.cooldown(2, 10, commands.BucketType.user)
    async def betrayaltogether(self, ctx):
        try:
            link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
        except:
            return await ctx.send("Error! Please join a voice channel.")

        embed=discord.Embed(
            title="Betrayal Together", 
            description=f"[Click Here]({link})", 
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['fishing'])
    @commands.cooldown(2, 10, commands.BucketType.user)
    async def fishingtogether(self, ctx):
        try:
            link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
        except:
            return await ctx.send("Error! Please join a voice channel.")

        embed=discord.Embed(
            title="Fishing Together", 
            description=f"[Click Here]({link})", 
            color=discord.Color.purple()
            )
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban (self, ctx, member:discord.User=None, reason=None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot ban yourself")
            return

        if reason == None:
            reason = "For being a jerk!"

        message = f"You have been banned from {ctx.guild.name} for {reason}"
        
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member} is banned by {ctx.author.name}!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User `{member}` has kicked by **{ctx.author.name}**.')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def tempmute(self, ctx, member: discord.Member,time):
        muted_role=discord.utils.get(ctx.guild.roles, name="Muted")
        time_convert = {"s":1, "m":60, "h":3600,"d":86400}
        tempmute= int(time[0]) * time_convert[time[-1]]

        await ctx.message.delete()
        await member.add_roles(muted_role)

        embed = discord.Embed(description= f"✅ **{member.display_name}#{member.discriminator} muted successfuly**", color=discord.Color.green())
 
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(tempmute)
        await member.remove_roles(muted_role)

    @commands.command()
    async def help(self, ctx):
        prefix = "!"

        embed = discord.Embed(
            title="Help command",
            desciption=f"My prefix is !",
            color=discord.Color.purple()
            )

        embed.add_field(name=prefix + "ban", value="ban member [member, reason]", inline=False)
        embed.add_field(name=prefix + "kick", value="kick member [member, reason]", inline=False)
        embed.add_field(name=prefix + "tempmute", value="temp mute a member [member, time]", inline=False)
        embed.add_field(name=prefix + "youtubetogether", value="play at youtube! `In vocal`", inline=False)
        embed.add_field(name=prefix + "pokertogether", value="play at poker game! `In vocal`", inline=False)
        embed.add_field(name=prefix + "chesstogether", value="play at chess game! `In vocal`", inline=False)
        embed.add_field(name=prefix + "betrayaltogether", value="play at betrayal game! `In vocal`", inline=False)
        embed.add_field(name=prefix + "fishingtogether", value="play at fishing game! `In vocal`", inline=False)
        embed.set_footer(text=self.bot.user)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(discordtogether(bot))
