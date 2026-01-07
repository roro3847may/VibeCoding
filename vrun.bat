@echo off
set "VP=C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding"
cd /d "%VP%"
cls
echo ==========================================
echo    Vibe Coding: Mobile System
echo ==========================================
echo.
python dash.py
echo.
echo [Running main.py...]
echo ------------------------------------------
python src\main.py
echo ------------------------------------------
echo.
echo Done. Type vhelp for commands.
echo ==========================================
