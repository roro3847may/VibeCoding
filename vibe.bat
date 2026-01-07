@echo off
if "%1"=="status" (
    python dash.py
) else if "%1"=="run" (
    python src/main.py
) else if "%1"=="test" (
    pytest
) else (
    echo Vibe Coding Utility
    echo Usage: vibe [status^|run^|test]
)
