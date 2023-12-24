### TOKEN ###
TOKEN = ''

### MESSAGES ###
WILLKOMMEN_MESSAGE = "Привет, сладкий. С чем ты к нам? Смеху хочешь или узнать чего?"
# Hello, dear. Why are here? Do you want a joke or know smth
UNKNOWN_MESSAGE = 'Дядя, я эту команду не знаю:' # Man, I don't know this command:
TAKE_FROG_MESSAGE = 'Держи жабу.' # Take the frog
STOP_TIMER_MESSAGE = "Пора на Донбасс!" # Time to Donbass
WRONG_COMMAND_MESSAGE = "Неправильное написание комманды, переделуй!" # That's wrong, do it again

### BUTTON QUERY MESSAGES ###

FROG_MESSAGE = "Дай ка жабу." # Give me frog
MEME_MESSAGE = "Смеха хочется, мир наскучил." # I want a joke, world is bored
VIDEO_MEME_MESSAGE = "Дай видео глянуть. Настроение на нуле." # Let me watch a video, I have low mood
WEATHER_MESSAGE = "Что у нас по погоде сегодня?" # What is the weather today?
QUESTION_CITY_MESSAGE = "Выбери интересующий городок." # Choice the city
ANSWER_WEATHER_MESSAGE = "Такова сейчас погода в городе {city}: {temp}." # Weather in ... is ... now
TIME_MESSAGE = "Каково сейчас время?" # What is the time?
CURRENCY_MESSAGE = "Ну как там с деньгами?" # What about money?
DOLLAR = 'Ну как "какими", долларами!' # How "what", dollars!
EURO = 'Ну как "какими", евро!' # How "what", euro!
CURRENCY_ANSWER_MESSAGE = "Тише-тише, деточка, вот курс:" # Quiet-quiet, dear, here is course
QUESTION_MESSAGE = "Какими деньгами?" # What money?
KEYBOARD_MESSAGE = "Вернемся же к начальной клавиатуре." # Let's return to the start keyboard
BOGDAN_MESSAGE = "Пиши правильно или к тебе придет дядя Богдан." # Write correctly or Uncle Bogdan will come to you.
MESSAGE_MESSAGE = "Хочу отправить сообщение." # I want to send a message.
MESSAGE_ANSWER_MESSAGE = "Хорошо, дорогой. Тогда я объясняю.\nЕсли тебе нужно отправить сообщение человеку, то вот шаблон:\nuser_id message\nВместо user_id пишешь id пользователя, message - сообщение.\nТолько адресат должен пользоватся мной. Иначе ... к тебе придет Богдан.\nТы можешь не знать как найти id человека. Смотри документацию."

### FORMATS ###
HTML = 'html'

### COMMANDS ###
START = 'start'

### PHOTOS & PHOTOS OPTIONS ##
PHOTO_MODE = 'rb'

### PATHES ###
MEME_PATH = './memes/'
VIDEO_PATH = './videos/'

### API QUERIES ###
GOOGLE = 'https://google.com/search?'
WEATHER_LINK = "https://ua.sinoptik.ua/погода-{city}"
DOLLAR_LINK = "https://minfin.com.ua/ua/currency/usd/"
EURO_LINK  =  'https://minfin.com.ua/ua/currency/eur/'
TELEGRAM_LINK = f"https://api.telegram.org/bot${TOKEN}/sendMessage"

### CITIES ###
CITIES = {"Киев" : "київ",                        "Харьков" : "харків",
          "Одесса" : "одеса",                     "Днепр" : "дніпро",
          "Донецк" : "донецьк",                   "Запорожье" : "запоріжжя",
          "Львов" : "львів",                      "Кривой Рог" : "кривий-ріг",
          "Николаев" : "миколаїв",                "Мариуполь" : "маріуполь",
          "Винница" : "вінниця",                  "Херсон" : "херсон",
          "Полтава" : "полтава",                  "Чернигов" : "чернігів",
          "Черкассы" : "черкаси",                 "Житомир" : "житомир",
          "Сумы" : "суми",                        "Хмельницкий" : "хмельницький",
          "Черновцы" : "чернівці",                "Ровно" : "рівне",
          "Ивано-Франковск" : "івано-франківськ", "Каменец-Подольский" : "кам'янець-подільський",
          "Тернополь" : "тернопіль",              "Луцк" : "луцьк",
          "Ужгород" : "ужгород"}
# This is the list of ukrainian cities

### REGEX ###
TIME = r"\d\d,\d\d"
USER_MESSAGE = r"(@[\d\w]+\s.+|-[\d\w]+\s.+|[\d\w]+\s.+)"
USERNAME = r"(@[\d\w]+|-[\d\w]+|[\d\w]+)"