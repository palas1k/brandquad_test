1. Зайти в .env поставить свои данные  
2. Написать в терминале make run  
3. Если make команды не поддерживаются написать docker compose up --build
4. Поменять в .env POSTGRES_HOST=* на POSTGRES_HOST=localhost
5. В терминале написать python manage.py createsuperuser для создания админа  
6. Поменять .env обратно и использовать админку  
*******
api/v1/swagger - ui для api  
POST api/v1/logs/ - запись в базу данных логов
GET api/v1/logs/ - получение всех записей из бд  
api/admin/ - админка