@echo off

:: Check if the input folder path is provided
if "%1"=="" (
    echo Usage: %~n0 [input_folder]
    exit /b
)

:: Set the folder containing the text files
set "input_folder=%~1"

:: Generate the output file name automatically
set "output_file=%input_folder%\merged_output_%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%.txt"

:: Clear the output file if it already exists
echo. > "%output_file%"

:: Loop through all .txt files in the folder
for %%f in ("%input_folder%\*.txt") do (
    echo ---------------------------------------- >> "%output_file%"
    echo File: %%~nxf >> "%output_file%"
    echo ---------------------------------------- >> "%output_file%"
    type "%%f" >> "%output_file%"
    echo. >> "%output_file%"
)

:: Notify completion
echo Merging complete. Output saved to "%output_file%".