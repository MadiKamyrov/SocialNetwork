# SocialNetwork

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/your-username/social-network.git

2. Перейдите в директорию проекта
cd socialnetwork

3. Создайте и активируйте виртуальное окружение
python -m venv env
env\Scripts\activate

4. Установите зависимости проекта
pip install -r requirements.txt

5. Выполните миграции и запустите сервер

Использование API (не забывайте вставлять токен в заголовок): 
Регистрация нового пользователя, POST запрос на  - URL: http://localhost:8000/users/
{
  "username": "example_user",
  "password": "example_password"
}

Аутентификация и получение токена доступа, POST запрос на - URL: http://localhost:8000/api/token/
{
  "username": "example_user",
  "password": "example_password"
}

Создание нового поста, POST запрос на -  URL: http://localhost:8000/api/post/
{
  "content": "This is a new post."
}

Получение списка постов - URL: http://localhost:8000/api/post/
Метод: GET

Вставка лайка на пост, POST запрос на - URL: http://localhost:8000/api/likes/
{
  "post": <post_id>
}

Удаление лайка, DELETE запрос на - URL: http://localhost:8000/api/likes/<like_id>/




