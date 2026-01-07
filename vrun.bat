@echo off
setlocal
set "vibePath=C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding"
cd /d "%vibePath%"

cls
echo ==========================================
echo    🚀 Vibe Coding: Starting Project...
echo ==========================================
echo.
python "%vibePath%\dash.py"
echo.
echo [Running main.py...]
echo ------------------------------------------
python "%vibePath%\src\main.py"
echo ------------------------------------------
echo.
echo Done. Type 'vhelp' for other commands.
echo ==========================================
endlocal
cd /d C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding
