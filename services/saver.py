import json
from datetime import datetime

from services.requester import LogsRequester
from src.models import LogsInfo


class LogsSaver:
    def __init__(self):
        self.file_name = 'nginx_json_logs.txt'

    def save_logs_in_db(self) -> None:
        result = LogsRequester().get_data_from_url()
        if result:
            self.file_name = result.file_name
        with open(self.file_name, 'r+') as f:
            result = [json.loads(x) for x in f.readlines()]
            for line in result:
                LogsInfo.objects.create(
                    ip_address=line.get('remote_ip'),
                    date_time=datetime.strptime(line.get('time'), "%d/%b/%Y:%H:%M:%S %z").strftime(
                        "%Y-%m-%d %H:%M:%S %z"),
                    http_method=line.get('request').split(' ')[0],
                    uri=line.get('request').split(' ')[1],
                    response_code=line.get('response'),
                    response_size=line.get('bytes'),
                )
