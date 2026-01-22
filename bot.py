import random
import discord
from discord.ext import commands

TOKEN = "BOT_TOKENİNİ_BURAYA_YAZ"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# 100 MESLEK VERİ TABANI
# =========================

CAREERS = {
    "TECHNOLOGY": [
        "SOFTWARE DEVELOPER","WEB DEVELOPER","MOBILE APP DEVELOPER","GAME DEVELOPER",
        "DATA ANALYST","DATA SCIENTIST","AI ENGINEER","CYBER SECURITY SPECIALIST",
        "CLOUD ENGINEER","DEVOPS ENGINEER","QA ENGINEER","EMBEDDED SYSTEMS ENGINEER",
        "NETWORK ENGINEER","SYSTEM ADMINISTRATOR","BLOCKCHAIN DEVELOPER",
        "AR/VR DEVELOPER","ROBOTICS ENGINEER","IT SUPPORT SPECIALIST",
        "DATABASE ADMINISTRATOR","TECHNICAL ARCHITECT"
    ],

    "CREATIVE": [
        "GRAPHIC DESIGNER","UI/UX DESIGNER","ILLUSTRATOR","ANIMATOR","GAME ARTIST",
        "CONCEPT ARTIST","PHOTOGRAPHER","VIDEOGRAPHER","VIDEO EDITOR",
        "MOTION DESIGNER","3D ARTIST","SOUND DESIGNER","MUSIC PRODUCER",
        "WRITER","SCREENWRITER","COPYWRITER","CONTENT CREATOR",
        "YOUTUBE CREATOR","STREAMER","SOCIAL MEDIA DESIGNER"
    ],

    "BUSINESS": [
        "ENTREPRENEUR","PROJECT MANAGER","PRODUCT MANAGER","MARKETING SPECIALIST",
        "DIGITAL MARKETER","SEO SPECIALIST","SALES MANAGER","BUSINESS ANALYST",
        "FINANCIAL ANALYST","ACCOUNTANT","ECOMMERCE MANAGER","BRAND MANAGER",
        "HR SPECIALIST","OPERATIONS MANAGER","INVESTMENT ADVISOR",
        "ECONOMIST","SUPPLY CHAIN MANAGER","LOGISTICS MANAGER",
        "CUSTOMER SUCCESS MANAGER","CONSULTANT"
    ],

    "HEALTH": [
        "DOCTOR","SURGEON","DENTIST","PHARMACIST","NURSE","PSYCHOLOGIST",
        "PSYCHIATRIST","PHYSIOTHERAPIST","DIETITIAN","VETERINARIAN",
        "RADIOLOGY TECHNICIAN","LABORATORY TECHNICIAN","PARAMEDIC",
        "EMERGENCY MEDICAL TECHNICIAN","OCCUPATIONAL THERAPIST",
        "SPEECH THERAPIST","SPORTS SCIENTIST","PUBLIC HEALTH SPECIALIST",
        "MEDICAL RESEARCHER","BIOTECHNOLOGIST"
    ],

    "ENGINEERING": [
        "MECHANICAL ENGINEER","ELECTRICAL ENGINEER","CIVIL ENGINEER",
        "COMPUTER ENGINEER","SOFTWARE ENGINEER","INDUSTRIAL ENGINEER",
        "AUTOMOTIVE ENGINEER","MECHATRONICS ENGINEER","AEROSPACE ENGINEER",
        "BIOMEDICAL ENGINEER","CHEMICAL ENGINEER","MATERIALS ENGINEER",
        "ENVIRONMENTAL ENGINEER","ENERGY SYSTEMS ENGINEER","ROBOTICS ENGINEER",
        "CONTROL SYSTEMS ENGINEER","TELECOMMUNICATIONS ENGINEER",
        "MANUFACTURING ENGINEER","NUCLEAR ENGINEER","PETROLEUM ENGINEER"
    ]
}

# =========================
# BOT EVENTLERİ
# =========================

@bot.event
async def on_ready():
    print(f"BOT AKTİF: {bot.user}")

# =========================
# KOMUTLAR
# =========================

@bot.command()
async def meslek(ctx, kategori: str = None):
    if kategori is None:
        kategori = random.choice(list(CAREERS.keys()))
    
    kategori = kategori.upper()

    if kategori not in CAREERS:
        await ctx.send("❌ GEÇERSİZ KATEGORİ\nKULLANILABİLİR: TECHNOLOGY, CREATIVE, BUSINESS, HEALTH, ENGINEERING")
        return

    meslek = random.choice(CAREERS[kategori])

    embed = discord.Embed(
        title="🎯 KARİYER ÖNERİSİ",
        description=f"**{meslek}**",
        color=discord.Color.blue()
    )
    embed.add_field(name="📂 KATEGORİ", value=kategori, inline=False)
    embed.set_footer(text="100 MESLEKLİ KARİYER BOTU")

    await ctx.send(embed=embed)

@bot.command()
async def kategoriler(ctx):
    embed = discord.Embed(
        title="📚 MEVCUT KATEGORİLER",
        description="\n".join(CAREERS.keys()),
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

# =========================
# BOT BAŞLAT
# =========================

bot.run(TOKEN)

