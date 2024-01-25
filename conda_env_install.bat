@echo off

:: Export the condabin path to PATH
set "PATH=%PATH%;C:\ProgramData\anaconda3\condabin"

:: Check for conda installation
where conda >nul 2>&1
if %errorlevel% neq 0 (
    echo Conda is not installed. Please install Anaconda or Miniconda first.
    exit /b 1
)

:: Create the conda environment
conda env create -n Image-Captioning -f environment.yml
if %errorlevel% neq 0 (
    echo Failed to create environment.
    exit /b 1
)

:: Activate the environment (optional)
:: conda activate Image-Captioning

echo Environment "Image-Captioning" created successfully!
