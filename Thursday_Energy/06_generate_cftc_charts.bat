@echo off
REM =========================================
REM Tuesday / Step 2 : Draw CFTC Graph
REM =========================================

REM この bat 自身のディレクトリ（Tuesday）
set CURRENT_DIR=%~dp0

REM root ディレクトリ
set ROOT_DIR=%CURRENT_DIR%..\

REM ---- 実行モード選択 ----
REM futuresonly / optioncombined
set POSITION_TYPE=futuresonly

REM ---- Python 実行 ----
python "%ROOT_DIR%common\draw_cftc_graph.py" %POSITION_TYPE%

pause
