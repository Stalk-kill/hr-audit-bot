@echo off
color 0A
echo =====================================
echo HR AUDIT BOT - DOUBLE CLICK START!
echo =====================================

pip install discord.py
notepad config.json

echo Starting bot...
python main.py
pause
