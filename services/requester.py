import requests


class LogsRequester:
    def __init__(self):
        self.url = 'https://drive.usercontent.google.com/u/0/uc?id=18Ss9afYL8xTeyVd0ZTfFX9dqja4pBGVp&export=download'
        self.file_name = "logs_file.txt"

    def get_data_from_url(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            return False
        with open(self.file_name, 'wb') as f:
            for i, chunk in enumerate(response.iter_content(32768)):
                if chunk:  # проверка конца файла
                    f.write(chunk)

            return True

