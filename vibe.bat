@echo off
setlocal
cd /d %~dp0

if "%1"=="status" (
    python dash.py
) else if "%1"=="chat" (
    python src/agent.py
) else (
    echo Vibe Coding Utility
    echo Usage: vibe [status^|chat]
)
endlocal
