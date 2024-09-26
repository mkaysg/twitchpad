@echo off
setlocal

title Twitchpad 0.5.0 - Setup
echo Twitchpad 0.5.0 - Setup

echo Cloning Twitchpad repository...

REM Set variables
set REPO_URL=https://github.com/mkaysg/twitchpad
set CONDA_ENV_NAME=twitchpad_env
set PYTHON_VERSION=3.9
set MINICONDA_EXE=%USERPROFILE%\miniconda3\Scripts\conda.exe
set MINICONDA_ACTIVATE_BAT=%USERPROFILE%\miniconda3\Scripts\activate.bat

REM Clone the example repository
git clone %REPO_URL%

echo Ensure that there's no errors after the repository is cloned.
echo.

REM Get the repository name from the URL (assuming the URL is in the standard format)
for %%F in (%REPO_URL%) do set "REPO_NAME=%%~nF"

REM Change to the newly cloned directory
cd "%REPO_NAME%"

echo Creating a new Miniconda Python 3.9 virtual environment named twitchpad_env
echo.

REM Create a new conda environment called twitchpad_env
%MINICONDA_EXE% create -y -n %CONDA_ENV_NAME% python=%PYTHON_VERSION%

echo Activating twitchpad_env as the active environment

REM Activate the new twitchpad_env environment
call %MINICONDA_ACTIVATE_BAT% %CONDA_ENV_NAME%

echo Installing twitchio and vgamepad packages. 
echo You will be prompted to enter 'y' to install the packages. Also, a Windows installer for a Virtual Controller will appear when installing vgamepad.
echo. 

pip install -r requirements.txt

echo --------------------------------------------------------------

echo If all the steps are successful, you are ready to start Twitchpad. To start, enter your OAUTH token, Channel name and preferred input syntax in config.ini. 
echo You will need to generate the OAUTH token first: https://twitchapps.com/tmi/
echo.

REM Open config.ini for user to enter their details
start notepad.exe config.ini

echo Once you've entered your details, double-click the Start_Twitchpad.bat file.
echo.
pause

endlocal
