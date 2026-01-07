@echo off
:: vrun.bat - 통합 실행 스크립트
set "VP=C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding"

:: 프로젝트 폴더로 이동
cd /d "%VP%"

:: 화면 초기화 및 환영 메시지
cls
echo ==========================================
echo    🚀 Vibe Coding: Mobile System
echo ==========================================
echo.

:: 시스템 상태 출력 (절대 경로 사용)
python "%VP%\dash.py"

echo.
echo [Running main.py...]
echo ------------------------------------------
:: 메인 코드 실행
python "%VP%\src\main.py"
echo ------------------------------------------
echo.
echo Done. Type 'vhelp' for commands.
echo ==========================================
