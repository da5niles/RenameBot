class Translation(object):
    START_TEXT = """Здравствуйте!
Это бот для переименования файлов через Telegram!

<b> Отправьте мне любой файл и ответьте на этот файл /rename NewName.apk </b>

/help для подробностей .."""
    RENAME_403_ERR = "Сожалею. Вам не разрешено переименовывать этот файл."
    ABS_TEXT = " Пожалуйста, не будь эгоистом."
    UPGRADE_TEXT = "<b>👉 Create own Clone Bot.. </b>  /help for Details"
    DOWNLOAD_START = "Скачиваю..."
    UPLOAD_START = "Загружаю"
    RCHD_TG_API_LIMIT = "Загружается за {} секунд. \nРазмер файла: {} \nИзвините. Но я не могу загружать файлы размером более 1,5 ГБ из-за ограничений Telegram API."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Готово! Забирай:**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Скачано за {} секунд. \n Загружено за {} секунд."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Миниатюра пользовательского файла сохранена. Это изображение будет использоваться в файле."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Персонализированный эскиз успешно удален."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Медиа успешно очищены."
    SAVED_RECVD_DOC_FILE = "Документ загружен успешно."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Пользовательский эскиз не найден."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """Привет, переименовать бота ..
    
1. Отправьте мне любой файл Telegram.
2. Ответьте на это сообщение /rename новое имя.расширение.
   
"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.."
    ABUSIVE_USERS = "Вам не разрешено использовать этого бота. Если вы считаете, что это ошибка, отметьте /me, чтобы снять это ограничение."
    FREE_USER_LIMIT_Q_SZE = """Невозможно обработать.
Бесплатные пользователи только 1 запрос за 30 минут.
/upgrade или Попробуйте через 1800 секунд."""
    IFLONG_FILE_NAME = """Максимальный размер имени файла, разрешенный Telegram, составляет {alimit} символов.
Данное имя файла содержит {число} символов.

<b> Эссе запрещено в имени файла Telegram! </b>
© ️ <code> @ReNameBot </code>
Сократите имя файла и повторите попытку!"""
