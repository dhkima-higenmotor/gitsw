pyinstaller --onefile --noconsole config.py
COPY /Y .\dist\config.exe .\
RMDIR /S /Q dist
RMDIR /S /Q build
DEL /Q config.spec

pyinstaller --onefile gitsw.py
COPY /Y .\dist\gitsw.exe .\
RMDIR /S /Q dist
RMDIR /S /Q build
DEL /Q gitsw.spec
