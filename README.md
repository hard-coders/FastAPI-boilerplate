# FastAPI - boilerplate

아래와 같은 일반적인 환경에서 FastAPI를 사용하기 위한 boilerplate입니다.

- MySQL
- SQLAlchemy
- uvicorn
- oauth2 로그인
- pip

테스트

- pytest

## 실행

```shell
$ docker-compose --env-file .env up -d
```

## 삭제

```shell
$ docker-compose down --rmi all --remove-orphans
```

## 테스트

```shell
$ pytest
```
