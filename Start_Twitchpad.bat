@echo off
setlocal

title Twitchpad 0.5.0 - Gamepad Inputs via Chat!
echo Twitchpad 0.5.0 - Gamepad Inputs via Chat!
echo Starting Twitchpad...

REM Set the environment name
set CONDA_ENV_NAME=twitchpad_env
set MINICONDA_ACTIVATE_BAT=%USERPROFILE%\miniconda3\Scripts\activate.bat

REM Activate the conda environment
call %MINICONDA_ACTIVATE_BAT% %CONDA_ENV_NAME%

REM Run the Python script
python twitchpad.py

REM Optional: Deactivate the environment after running the script
conda deactivate
pause

endlocal
