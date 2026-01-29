@echo off
setlocal

REM ==============================
REM 開きたいURL
REM ==============================
set TARGET_URL=https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm

REM ==============================
REM Python スクリプト実行
REM ==============================
set CURRENT_DIR=%~dp0

REM root ディレクトリ
set ROOT_DIR=%CURRENT_DIR%..\

REM common/access_site.py を実行
python "%ROOT_DIR%common\access_site.py" "%TARGET_URL%"

endlocal
