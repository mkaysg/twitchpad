@echo off
setlocal

REM Set the environment name
set CONDA_ENV_NAME=twitchpad_env

REM Activate the conda environment
call C:\Miniconda3\Scripts\activate.bat %CONDA_ENV_NAME%

REM Run the Python script
python twitchpad.py

REM Optional: Deactivate the environment after running the script
conda deactivate

endlocal
