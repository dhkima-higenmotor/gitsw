REM pyinstaller --onefile --noconsole config.py
pyinstaller --noconsole --upx-dir=%userprofile%\scoop\apps\upx\current config.py

REM COPY /Y .\dist\config.exe .\
REM RMDIR /S /Q dist
REM RMDIR /S /Q build
REM DEL /Q config.spec

REM pyinstaller --onefile gitsw.py
pyinstaller --upx-dir=%userprofile%\scoop\apps\upx\current gitsw.py

REM COPY /Y .\dist\gitsw.exe .\
REM RMDIR /S /Q dist
REM RMDIR /S /Q build
REM DEL /Q gitsw.spec
