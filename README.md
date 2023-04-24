# gitsw

_솔리드웍스 기구설계 버전관리용 Git Client_

## 기본 소프트웨어 설치

### 1. Git for Windows Portable
* D:\UTIL 폴더 생성
* https://git-scm.com/download/win 에서 64-bit Git for Windows Portable 을 다운로드
* 다운로드 받은 파일을 D:\UTIL 폴더로 이동
* 이동한 파일을 더블클릭하여 압축 해제
* 압축해제된 폴더 경로를 D:\UTIL\Git으로 변경

### 2. Github CLI
* https://cli.github.com/ 에서 Download for Windows 버튼을 눌러서 msi 파일 다운로드
* 다운로드 받은 msi 파일을 더블클릭하여 설치
* 설치장소는 원래의 기본 설치 경로 권장 :  C:\Program Files\GitHub CLI\
* 인증환경변수 : GH_TOKEN


### 3. Windows Terminal
* MS Windows 10 에는 기본설치가 안 되어 있으므로 Microsoft Store에서 찾아서 직접 설치할 것
* MS Windows 11 에는 기본적으로 설치되어 있음
* 실행명령어 : `wt.exe`
* 신규 프로필 설정 : git-cmd
  - 이름 : `git-cmd`
  - 명령줄 : `D:\UTIL\Git\git-cmd.exe`
  - 시작 디렉토리 : `D:\`
  - 아이콘 : `D:\UTIL\Git\mingw64\share\git\git-for-windows.ico`

* 신규 프로필 설정 : git-bash
  - 이름 : `git-bash`
  - 명령줄 : `D:\UTIL\Git\git-bash.exe -i -l`
  - 시작 디렉토리 : `D:\`
  - 아이콘 : `D:\UTIL\Git\mingw64\share\git\git-for-windows.ico`

## Config

* 환경변수 등록

```
GH_TOKEN = <github_token>
```

* git global 설정

```
git config --global user.email "...@higenmotor.com"
git config --global user.name "..."
git config --global color.ui auto
git config --global core.editor 'code'
git config --global credential.helper cache
git config --global push.default matching
git config --global init.defaultBranch main
```

* github CLI 설정

```
gh config set editor "code -w"
gh config set git_protocol https
gh auth login
```
