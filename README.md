## Telegram Bot Starter Kit
This repository contains a basic template for creating a Telegram bot using Python. You can use this as a starting point to build your own custom Telegram bot.

### Prerequisites
Before you begin, make sure you have the following installed:

- Python 3.x

#### Requirements
- Django
- telethon 
- load_dotenv
- gunicorn

#### Setup:
- Clone the repository or download the source code.
```
git@github.com:Graystone-Premium/telergram.git
```
- go to main directory
```
cd telergram
```
- Install the required dependencies.
```
pip install -r requirements.txt
```
Open teleBot.py under folder and replace api_id and api_hash  with the API token you received from telegram API.

### Run the Django web app
To run project on locally :

- create a .env file in project directory and set
```
MYPROJECT_ENV=dev
```

```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py createsuperuser
```
```
python manage.py runserver
```
5. Access the Price Matching Tools by visiting http://localhost:8000/ in your web browser.
### Run Your Bot:
```
python bot/teleBot.py
```
Your bot should now be running and and it will save the message on database.

### Contributing
Feel free to contribute to this project by creating pull requests or reporting issues. Your contributions are welcome!

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
python-telegram-bot library for making Telegram bot development easier.