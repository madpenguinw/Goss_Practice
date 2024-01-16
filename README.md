# Практическое задание
В рамках обучения на магистратуре ИТМО по направлению __"Веб-технологии"__

# Запуск проекта в Docker контейнере
```bash
- git clone https://github.com/madpenguinw/Goss_Practice
- добавить в корень проекта файл env_vars.sh с переменными окружения
- запустить docker
- docker build -t goss_practice .
- запустить VPN с сервером, находящимся не в РФ
- docker run -p 8080:8080 goss_practice
```
Или можно использовать уже готовый образ с Docker-Hub
```bash
- docker pull penguinw/goss_practice:latest
- docker run -p 8080:8080 goss_practice
```

# Пример заполнения файла env_vars.sh
```bash
export MONGO_DB_NAME=ITMO
export MONGO_WEBS_COLLECTION=goss_practice
export MONGO_USER=lmikhailsokolovl
export MONGO_PASSWORD=qysjsEqJWQoNsvrn
export PORT=8080
```

## Автор
**Соколов Михаил, студент группы P4208**
