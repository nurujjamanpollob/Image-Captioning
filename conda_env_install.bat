@echo off
:: Export the condabin path to PATH
set "PATH=%PATH%;C:\ProgramData\anaconda3\condabin"
set environment_name=Image-Captioning

:: Check for existing environment
conda env list | findstr /I "%environment_name%" >nul
if %errorlevel% equ 0 (
    echo Environment "%environment_name%" already exists.
    set /p choice="Do you want to activate, delete, or create a new environment? (activate/delete/create): "
    if /i "%choice%" equ "activate" (
        conda activate %environment_name%
        echo Environment "%environment_name%" activated successfully.
    ) else if /i "%choice%" equ "delete" (
        call :delete_environment
    ) else if /i "%choice%" equ "create" (
        echo Creating a new environment named "%environment_name%"...
        conda create --name %environment_name% python=3.9 :: Example package installation
        if %errorlevel% equ 0 (
            echo Environment "%environment_name%" created successfully.
        ) else (
            echo Error creating environment "%environment_name%". Please check for issues.
        )
    ) else (
        echo Invalid choice. Please choose "activate", "delete", or "create".
    )
) else (
    echo Environment "%environment_name%" does not exist.
    echo Creating environment "%environment_name%"...
    conda env create --name %environment_name% --file environment.yml
        if %errorlevel% equ 0 (
            echo Environment "%environment_name%" created successfully.
        ) else (
            echo Error creating environment "%environment_name%". Please check for issues.
            :: Delete the environment if it was created
            call :delete_environment
        )

    echo Activating environment "%environment_name%"...
    conda activate %environment_name%

    :: Show instruction to run the project
    echo Environment "%environment_name%" created and activated successfully!
    echo To run the project, run the following command:
    echo python main.py
    echo To deactivate the environment, run the following command:
    echo conda deactivate
    echo To delete the environment, run the following command:
    echo conda remove --name %environment_name% --all
    echo To update the environment, run the following command:
    echo conda env update --name %environment_name% --file environment.yml --prune
    echo To update the environment and dependencies, run the following command:
    echo conda env update --name %environment_name% --file environment.yml --prune && pip install -r requirements.txt --index-url https://download.pytorch.org/whl/cu121

    )
)

goto :eof

:delete_environment
    conda env remove --name %environment_name%
    if %errorlevel% equ 0 (
        echo Environment "%environment_name%" successfully deleted.
    ) else (
        echo Error deleting environment "%environment_name%". Please check for issues.
    )
    goto :eof
