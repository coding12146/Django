# 📌 사전과제 : 업무(Task) 시스템 요구사항

## 📍 시나리오 설명
김윙크 사원이 단비교육에 입사하여 업무를 할당받았습니다. 김윙크 사원은 다른 팀들과 협업하여 업무를 처리해야 합니다. 업무(Task)를 생성하고 관리하는 시스템을 개발해야 합니다. 다음은 시스템의 요구사항입니다.
단비, 다래, 블라블라, 철로, 땅이, 해태, 수피 7개의 팀
이를 위해 김윙크 사원은 업무(Task)를 생성해야 합니다. 업무(Task)생성 시, 협업이 필요한 팀을 하위업무(SubTask)로 설정하면 해당 팀들에게 
업무를 요청할 수 있게됩니다.

## 📍 조건
- 업무 생성 시, 한 개 이상의 팀을 설정해야합니다.
- 단, 업무(Task)를 생성하는 팀이 반드시 하위업무(SubTask)에 포함되지는 않습니다.
- ex) 단비 Team이 업무(Task) 생성 시 하위 업무로 단비, 다래, 철로 Team을 설정할 수 있습니다. 단, 단비팀이 업무를 진행하지 않아도 
될 경우에는 꼭 하위업무에 단비팀이 들어가지 않아도 됩니다.
- 단, 정해진 7개의 팀 이외에는 다른 팀에 하위업무(SubTask)를 부여할 수 없습니다.
- 업무(Task)를 수정할 경우 하위업무(SubTask)의 팀들도 수정 가능합니다. 단, 완료된 하위업무(SubTask)에 대해서는 삭제처리는 불가능합니 
다.
- ex) 단비 Team이 업무(Task) 생성 시 하위 업무(SubTask)단비, 다래, 철로 Team을 설정 후 하위업무팀을 단비만 하도록 하거나 단비, 다 
래, 수피 팀으로 유동적으로 변경가능합니다. 변경시 완료된 하위업무(SubTask) 있다면 무시합니다.
- 업무(Task)는 작성자 이외에 수정이 불가합니다.
- 업무(Task)에 할당된 하위업무(SubTask)의 팀(Team)은 수정, 변경 가능해야 합니다. 단 해당 하위업무(SubTask)가 완료되었다면 삭제되지 
않아야 합니다.

- 업무(Task) 조회 시 하위업무(SubTask)에 본인 팀이 포함되어 있다면 업무목록에서 함께 조회가 가능해야합니다. 
- 업무(Task) 조회 시 하위업무(SubTask)의 업무 처리여부를 확인할 수 있어야 합니다.

- 업무(Task)의 모든 하위업무(SubTask)가 완료되면 해당 상위업무(Task)는 자동으로 완료처리가 되어야합니다. 
- 하위업무(SubTask) 완료 처리는 소속된 팀만 처리 가능합니다.

## 📍 DB 스키마
### Task
- id ( )
- create_user ()
- team ( )
- title ( )
- content ( )
- is_complete (  , default=False)
- completed_date (  )
- created_at ( )
- modified_at ( )
### SubTask 
- id ( ) 
- team ( )
- is_complete (  , default=False) 
- completed_date (  )
- created_at ( ) 
- modified_at ( ) 
### USER(abstract)
- id ( )
- username ( ) 
- pw ( )
- team ()

## 📍 FAQ
- 데이터베이스 구조를 변경해도 되나요?
- 본인이 생각하는 최적의 구조로 변경해도 됩니다. 단, 필드명 변경시 확인이 가능한 이름이 필요합니다. 
- 라이브러리를 사용해도 작성해도 되나요?
- 작업에 필요하다고 판단되면 사용하셔도 됩니다. 
- 회원가입과 로그인 내용을 꼭 구현해야하나요?
- 필수 요소는 아닙니다. 필요하다면 구현해주시면 됩니다.

- 제약사항
Python, Django, DRF를 이용해 구현해 주세요.
- 작업 버전
- djangorestframework>3.0 
- django>3.2
- python>3.9
- Database의 사용은 자유롭게 하시면 됩니다. 
- Restful API로 구현해 주세요.
- 명시된 예시 외 필요하다고 생각되는 API는 자유롭게 구현해 주세요. 
- 테스트 코드를 '꼭' 작성해 주세요.

# 📌 중점 확인 사항
- 기능이 의도대로 동작하는지 확인합니다. 
- 테스트 코드의 동작을 확인합니다.
- 데이터베이스 쿼리 로깅 옵션을 켜고 비효율적인 쿼리가 발생하는지 확인합니다. 
- 프로젝트의 구성이 올바른지 확인합니다.
- 소스코드의 구성이 가독성있게 구성되어 있는지 확인합니다.

## 📍 주요 기능
### 업무(Task) 생성

- 업무 생성 시, 한 개 이상의 팀을 설정해야합니다.
![image](https://github.com/maxkim77/preassignment_FE/blob/19fe351efde66c9ddc254d7e137b9a7251012453/image/01.gif)


- 업무(Task)를 생성하는 팀이 반드시 하위업무(SubTask)에 포함되지는 않습니다. 단비 Team이 업무(Task) 생성 시 하위 업무로 단비, 다래, 철로 Team을 설정할 수 있습니다. 단, 단비팀이 업무를 진행하지 않아도 될 경우에는 꼭 하위업무에 단비팀이 들어가지 않아도 됩니다.

![02](https://github.com/maxkim77/preassignment_FE/assets/141907655/de666b30-ca5f-4408-b9d0-87d75db09573)

- 단, 정해진 7개의 팀 이외에는 다른 팀에 하위업무(SubTask)를 부여할 수 없습니다.
![03](https://github.com/maxkim77/preassignment_FE/assets/141907655/af02ebb3-0914-4443-aa35-0788a5a0011c)

### 업무(Task) 수정 및 삭제
- 업무(Task)를 수정할 경우 하위업무(SubTask)의 팀들도 수정 가능합니다.


ex) 단비 Team이 업무(Task) 생성 시 하위 업무(SubTask)단비, 다래, 철로 Team을 설정 후 하위업무팀을 단비만 하도록 하거나 단비, 다 
래, 수피 팀으로 유동적으로 변경가능합니다. 변경시 완료된 하위업무(SubTask) 있다면 무시합니다.
![수정01](https://github.com/maxkim77/preassignment_FE/blob/37d8b89786ac4ae8ef075a5b06bf4dec2a9ec066/image/%EC%88%98%EC%A0%9501.gif)
![업무 수정](https://github.com/maxkim77/pre_assignment/blob/6ee74c0c5b9bdd259ed1c51d5090e9f461897220/image/2.gif)


<스웨거 문서에서도 확인>


- 단, 완료된 하위업무(SubTask)에 대해서는 삭제처리는 불가능합니다.
![수정02](https://github.com/maxkim77/preassignment_FE/blob/37d8b89786ac4ae8ef075a5b06bf4dec2a9ec066/image/%EC%88%98%EC%A0%9502.gif)
- 업무(Task)는 작성자 이외에 수정이 불가합니다.
![수정03](https://github.com/maxkim77/preassignment_FE/blob/37d8b89786ac4ae8ef075a5b06bf4dec2a9ec066/image/%EC%88%98%EC%A0%9503.gif)

### 업무(Task) 조회
- 업무(Task) 조회 시 하위업무(SubTask)에 본인 팀이 포함되어 있다면 업무목록에서 함께 조회가 가능해야합니다.
![조회01](https://github.com/maxkim77/preassignment_FE/blob/37d8b89786ac4ae8ef075a5b06bf4dec2a9ec066/image/%EC%A1%B0%ED%9A%8C01.gif)
- 업무(Task) 조회 시 하위업무(SubTask)의 업무 처리여부를 확인할 수 있어야 합니다.
![조회02](https://github.com/maxkim77/preassignment_FE/blob/37d8b89786ac4ae8ef075a5b06bf4dec2a9ec066/image/%EC%A1%B0%ED%9A%8C02.PNG)
![업무 조회](https://github.com/maxkim77/pre_assignment/blob/6ee74c0c5b9bdd259ed1c51d5090e9f461897220/image/3.PNG)
### 업무(Task) 완료 처리
- 업무(Task)의 모든 하위업무(SubTask)가 완료되면 해당 상위업무(Task)는 자동으로 완료처리가 되어야합니다.
![완료01](https://github.com/maxkim77/preassignment_FE/blob/37d8b89786ac4ae8ef075a5b06bf4dec2a9ec066/image/%EC%99%84%EB%A3%8C01.gif)
- 하위업무(SubTask) 완료 처리는 소속된 팀만 처리 가능합니다.
![완료02](https://github.com/maxkim77/preassignment_FE/blob/6358089c4461a4af97374a259b7766f4a66f9d10/image/%EC%99%84%EB%A3%8C%202.gif)

### 회원 기능
- 회원가입, 로그인, 로그아웃 기능을 처리합니다.
![회원](https://github.com/maxkim77/preassignment_FE/blob/6358089c4461a4af97374a259b7766f4a66f9d10/image/%ED%9A%8C%EC%9B%90.gif)
## 테스트코드 작성 및 쿼리 로깅 옵션 포함
- 테스트 코드 통과


   ![테스트](https://github.com/maxkim77/pre_assignment/blob/c8e94aef7a2fc2521e3a362c7c5795e60b358ead/image/5.PNG)

- settings.py 로깅 옵션 추가


```
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}
```


## 📍 프로젝트 구성
### 프로젝트 구조 
```
📦project
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂project
 ┣ 📂task
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.env
 ┣ 📜db.sqlite3
 ┣ 📜debug.log
 ┗ 📜manage.py
📦 FE
```
### 📍 데이터베이스 설계 
![db](https://github.com/maxkim77/pre_assignment/blob/ab1a28b96ec1959b46da327e2dfce699895fda3f/image/6.png)

- 작업(Task)과 팀(Team) 간의 관계는 다대다 관계
- 사용자(User)와 팀(Team) 간의 관계는 다대일 관계

### 📍 API 명세 및 URL
- Task


| 엔드포인트                  | URL                                | 메서드 | 설명                                 |
|---------------------------|------------------------------------|--------|--------------------------------------|
| Task 목록 조회            | `/task/tasks/`                      | GET    | 모든 업무(Task) 목록 조회              |
| Task 생성                 | `/task/tasks/`                      | POST   | 새로운 업무(Task) 생성                |
| Task 상세 조회            | `/task/tasks/{task_id}/`            | GET    | 특정 업무(Task)의 상세 정보 조회      |
| Task 수정                 | `/task/tasks/{task_id}/`            | PUT    | 특정 업무(Task) 수정                  |
| Task 완료                 | `/task/tasks/{task_id}/complete/`   | POST   | 특정 업무(Task) 완료 처리              |
| SubTask 생성              | `/task/tasks/{task_id}/subtasks/`   | POST  | 특정 업무(Task)에 하위업무(SubTask) 생성 |
| SubTask 목록 조회         | `/task/tasks/{task_id}/subtasks/`   | GET   | 특정 업무(Task)의 하위업무(SubTask) 목록 조회 |
| SubTask 상세 조회         | `/task/tasks/{task_id}/subtasks/{subtask_id}/`| GET | 특정 하위업무(SubTask)의 상세 정보 조회 |
| SubTask 수정              | `/task/tasks/{task_id}/subtasks/{subtask_id}/`| PUT | 특정 하위업무(SubTask) 수정 |
| SubTask 완료 처리         | `/task/tasks/{task_id}/subtasks/{subtask_id}/complete/`| POST | 특정 하위업무(SubTask) 완료 처리 |


- accounts


#### accounts 엔드포인트:

| 엔드포인트              | URL                      | 메서드 | 설명                                 |
|-----------------------|--------------------------|--------|--------------------------------------|
| User 목록 조회       | `/signup/`               | GET    | 모든 사용자(User) 목록 조회          |
| 사용자 회원가입      | `/user/`                 | POST   | 새로운 사용자(User) 회원가입                  |
| 사용자 로그인        | `/token/`                | POST   | 사용자(User) 로그인                            |
| Team 목록 조회      | `/token/refresh/`        | GET    | 모든 팀(Team) 목록 조회              |
| jwt 토큰 검증       | `/token/verify/`         | POST   | jwt 토큰 검증              |


#### URL:
- 📦 BE : https://github.com/maxkim77/preassignment
- 📦 FE : https://github.com/maxkim77/preassignment_FE
- 📅 WBS : https://github.com/users/maxkim77/projects/5
  
## 📍 실행방법
```
manage.py와 같은 위치에 아래와 같이 .env 파일 생성
SECRET_KEY=Your_KEY
DEBUG=True

python -m venv venv
./venv/Scripts/activate or source venv/bin/activate
(venv) pip install -r requirements.txt
(venv) python.exe -m pip install --upgrade pip (필요시)
(venv) python manage.py runserver
(venv) cd project
(venv) PS C:\Users\PC_1M\바탕 화면\preassignment\project> python manage.py makemigrations
(venv) PS C:\Users\PC_1M\바탕 화면\preassignment\project> python manage.py migrate
(venv) PS C:\Users\PC_1M\바탕 화면\preassignment\project> python manage.py runserver

```

## 📍 에러 및 해결 과정 정리
1. 에러명: Reverse accessor clashes (fields.E304)
- 에러 상황:
auth.User.groups 및 auth.User.user_permissions 필드가 user.CustomUser.groups 및 user.CustomUser.user_permissions 필드와 충돌.
- 에러 해결법:
CustomUser 모델의 groups 및 user_permissions 필드에 related_name 옵션을 'custom_users'로 설정.
Task 모델의 create_user 필드의 related_name 변경.


2. 에러명: Relation with swapped model (fields.E301)
- 에러 상황:
task.Task.create_user 필드가 auth.User 모델과 관계를 맺고 있지만, settings.AUTH_USER_MODEL로 업데이트되지 않음.
- 에러 해결법:
Task 모델의 create_user 필드를 settings.AUTH_USER_MODEL을 사용하도록 수정하고 데이터베이스 마이그레이션 수행.


3. 에러명: IntegrityError at /task/tasks/
- 에러 상황:
Task 객체 생성 시 "NOT NULL constraint failed: task_task.create_user_id" 오류 발생. create_user 필드가 null 값을 허용하지 않음.
- 에러 해결법:
Task 모델의 create_user 필드를 null=True, blank=True로 설정하여 null 값을 허용하도록 변경. 데이터베이스 마이그레이션 수행.
TaskListView의 perform_create 메서드 수정하여 생성 시 요청한 사용자를 create_user로 설정.

