@echo off
REM Agregar todos los archivos al staging area
git add .

REM Hacer el commit con un mensaje predeterminado
git commit -m "Auto commit"

REM Hacer el push al repositorio remoto
git push origin Suspension

REM Pausa para ver los resultados
pause
