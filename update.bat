@echo off
set /P "updates=What have you changed? "
git add .
git commit --allow-empty --allow-empty-message -m "%updates%"
git push
echo Now wait until it finishes building. It takes like 15-30 seconds
pause