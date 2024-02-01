@echo off

:: Check for pip installation
where pip >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Please install Python first.
    exit /b 1
)

:: Create the virtual environment
python -m venv Image-Captioning
if %errorlevel% neq 0 (
    echo Failed to create virtual environment.
    exit /b 1
)

:: Install dependencies
pip install -r requirements.txt --index-url https://download.pytorch.org/whl/cu121
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    exit /b 1
)

:: Activate the environment
call Image-Captioning\Scripts\activate.bat

echo Environment "Image-Captioning" created and dependencies installed successfully!
