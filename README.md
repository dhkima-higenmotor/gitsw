# gitsw

_Github Client for Sloidworks_

## Concept
* Simple & Minimal
* Focus on Solidworks
* Use LFS
* Forced merge (but Risky)
* Co-work other clients (Tortoise-git, git-fork ...)

## Todo
* Debug
* Lock
* Cutout external dependancies
* Improved merge
* Apply Forgejo API

## Manual
* [Manual](Manual/README.md)


## 설계
* **mygit.py** : 기본설정파일 읽기, git 명령모음
* **mysw.py** : 솔리드웍스 명령 모음
  - 어셈블리 파일 트리 추출
  - 솔리드웍스 실행
  - 

* **mygithub** : github 명령모음
  - 원격 repo 생성, LFS 설정 웹페이지 열기, repo init, clone
  - 원격 repo 리스트 추출
  - 팀원 명단 읽기


# LFS Enabling by API

* Ref : https://docs.github.com/ko/rest/repos/lfs?apiVersion=2022-11-28#enable-git-lfs-for-a-repository
* `admin:enterprise` token is needed.

```
gh api --method PUT -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" /repos/mech-higenmotor/TEST/lfs

curl -L -X PUT -H "Accept: application/vnd.github+json" -H "Authorization: Bearer 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" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/mech-higenmotor/TEST/lfs
```
