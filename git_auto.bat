@echo off

REM Agregar todos los archivos al staging area
git add .

REM Solicitar al usuario que ingrese el mensaje de commit
set /p commitMessage="Ingrese el mensaje de commit: "

REM Hacer el commit con el mensaje personalizado
git commit -m "%commitMessage%"

REM Hacer el push al repositorio remoto
git push

REM Pausa para ver los resultados
pause
