# FastAPI - boilerplate

아래와 같은 일반적인 환경에서 FastAPI를 사용하기 위한 boilerplate입니다.

- MySQL
- SQLAlchemy
- uvicorn
- oauth2 로그인
- pip

테스트

- pytest

## 사전 작업

### 환경변수 설정

e.g.

```dotenv
# example .env file
SECRET_KEY=64c27589c590ada80f0c04a7232581f45b8168defae9e3bdba0d655ceee77ee8
DB_HOST=db
DB_PORT=3306
DB_USER=root
DB_PASSWORD=1234
DB_DATABASE=dev
```

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
