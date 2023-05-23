@echo off
set /P "updates=What have you changed? "
git add .
git commit --allow-empty --allow-empty-message -m "%updates%"
git push