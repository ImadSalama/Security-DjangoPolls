# Security-DjangoPolls
This repository is cloned from Django Tutorial using JSON data only
it is basic data usage to test the behavior of django 3.2 with
security vulnerability with no business logic inside it.

## APIs

1. `GET http://localhost/polls` to get the data of the polls

2. `POST http://localhost/polls` to add new question the body should countain the following:
```json
{
    "question_text": "Hello what are you doing ?",
    "pub_date": "2022-12-06T22:15:16"
}
```

