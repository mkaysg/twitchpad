@echo off
setlocal

title Twitchpad - Updater
echo Twitchpad - Updater

REM Pull the latest updates from the repo
echo Obtaining the latest Twitchpad updates from github...
git pull

echo Update completed!

echo.
pause

endlocal