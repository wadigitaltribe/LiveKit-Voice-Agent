@echo off
title Voice Agent Startup

echo ==========================================
echo  Voice Agent Environment Setup
echo ==========================================
echo.

echo Installing core dependencies...
:: THE FIX: Removed google, added openai
pip install python-dotenv==1.2.1 livekit-agents==1.5.7 livekit-plugins-deepgram==1.5.7 livekit-plugins-openai==1.5.7 livekit-plugins-elevenlabs==1.5.7 livekit-plugins-silero==1.5.7

echo.
echo ==========================================
echo  Starting the LiveKit Agent...
echo ==========================================
echo.

:: Run the agent
python main.py dev

:: Keep the window open if the agent crashes or is stopped
pause