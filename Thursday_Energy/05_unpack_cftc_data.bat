@echo off
REM =========================================
REM Tuesday / Step 1 : unpacker
REM =========================================

REM この bat 自身の位置（Tuesday）
set CURRENT_DIR=%~dp0

REM root ディレクトリ
set ROOT_DIR=%CURRENT_DIR%..\

REM common/unpacker.py を実行
python "%ROOT_DIR%common\unpacker.py"

pause
