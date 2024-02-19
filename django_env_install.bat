@echo off

:: Define the environment and app name
set project_name=restapi

:: Check for django-admin installation
where django-admin >nul 2>&1
if %errorlevel% neq 0 (
    echo django-admin is not installed. Please install Django first.
    exit /b 1
)

:: Create the Django project
django-admin startproject %project_name%
if %errorlevel% neq 0 (
    echo Failed to create Django project.
    exit /b 1
)

echo Django project "myproject" created successfully!