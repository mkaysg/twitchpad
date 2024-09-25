@echo off
setlocal

REM Set variables
set MINICONDA_INSTALLER=Miniconda3-latest-Windows-x86_64.exe
set CONDA_ENV_NAME=twitchpad_env
set PYTHON_VERSION=3.9
set GIT_INSTALLER=Git-2.40.0-64-bit.exe
set REPO_URL=https://github.com/example/repo.git  REM Replace with your desired repo URL

REM Download Miniconda installer if it doesn't exist
if not exist "%MINICONDA_INSTALLER%" (
    echo Downloading Miniconda...
    powershell -Command "Invoke-WebRequest -Uri https://repo.anaconda.com/miniconda/%MINICONDA_INSTALLER% -OutFile %MINICONDA_INSTALLER%"
)

REM Install Miniconda silently
start /wait %MINICONDA_INSTALLER% /S /D=C:\Miniconda3

REM Add Miniconda to PATH
set "PATH=C:\Miniconda3;C:\Miniconda3\Scripts;%PATH%"

REM Delete Miniconda Installer
del %MINICONDA_INSTALLER%

REM Initialize conda
C:\Miniconda3\Scripts\conda.exe init

REM Create a conda environment with a specific Python version
conda create -y -n %CONDA_ENV_NAME% python=%PYTHON_VERSION%

REM Activate the conda environment
call C:\Miniconda3\Scripts\activate.bat %CONDA_ENV_NAME%

REM Check if requirements.txt exists and install packages
if exist requirements.txt (
    echo Installing packages from requirements.txt...
    pip install -r requirements.txt
) else (
    echo requirements.txt not found. Skipping package installation.
)

REM Download Git installer if it doesn't exist
if not exist "%GIT_INSTALLER%" (
    echo Downloading Git...
    powershell -Command "Invoke-WebRequest -Uri https://github.com/git/git/releases/latest/download/%GIT_INSTALLER% -OutFile %GIT_INSTALLER%"
)

REM Install Git silently
start /wait %GIT_INSTALLER% /VERYSILENT /NORESTART

REM Clone the example repository
git clone %REPO_URL%

echo Miniconda installation, environment setup, package installation, and Git setup complete.
echo To start, configure the config.ini first with your OAUTH token, Channel name and preferred input syntax. Then run the Start_Twitchpad.bat file.
echo You will need to generate the OAUTH token: https://twitchapps.com/tmi/

REM Get the repository name from the URL (assuming the URL is in the standard format)
for %%F in (%REPO_URL%) do set "REPO_NAME=%%~nF"

REM Change to the newly cloned directory
cd "%REPO_NAME%"
start notepad.exe config.ini

endlocal
