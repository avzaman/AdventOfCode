@echo off

REM Activate the Conda environment
call conda activate rapids-23.12

REM Run the Python script
python DayTwentyfive.py

REM Deactivate the Conda environment
call conda deactivate