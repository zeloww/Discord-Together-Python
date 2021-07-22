import discord
from discord.ext import commands
from discordTogether import DiscordTogether

class discordtogether(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.togetherControl = DiscordTogether(bot)

    @commands.command(aliases=['youtube'])
    async def youtubetogether(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')

        embed=discord.Embed(
            title="Youtube Together", 
            description=f"[Click Here]({link})", 
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['poker'])
    async def pokertogether(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'poker')

        embed=discord.Embed(
            title="Poker Together", 
            description=f"[Click Here]({link})", 
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['chess'])
    async def chesstogether(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'chess')

        embed=discord.Embed(
            title="Chess Together", 
            description=f"[Click Here]({link})", 
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['betrayal'])
    async def betrayaltogether(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')

        embed=discord.Embed(
            title="Betrayal Together", 
            description=f"[Click Here]({link})", 
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['fishing'])
    async def fishingtogether(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')

        embed=discord.Embed(
            title="Fishing Together", 
            description=f"[Click Here]({link})", 
            color=discord.Color.purple()
            )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(discordtogether(bot))
