import os
import re
from datetime import datetime


class MessageReader:

    __kakaotalk_datetime_pattern_dict = {'window_ko_date': "-{15} [0-9]{4}년 [0-9]{1,2}월 [0-9]{1,2}일 \S요일 -{15}",
                                    'window_ko_time': "((\[)([^\[])+(\])) ((\[오)\S [0-9]{1,2}:[0-9]{1,2}(\]))",
                                    'android_ko': "([0-9]){4}년 ([0-9]){1,2}월 ([0-9]){1,2}일 (오전|오후) ([0-9]){1,2}:([0-9]){1,2}",
                                    'android_en': "([A-z])+ ([0-9]){1,2}, ([0-9]){4} at ([0-9]){1,2}:([0-9]){1,2}\s(AM|PM)",
                                    }

    def __init__(self, directory: str, filename: str):
        self.__directory = directory
        self.__filename = filename
    
    def get_messages(self) -> list:
        self.__validateFileExistence()
        file_path = os.path.join(self.__directory, self.__filename)
        file_type = self.__check_export_file_type(file_path)
        return self.__parse(file_type, file_path)

    def __validateFileExistence(self):
        if not os.path.exists(self.__directory):
            raise Exception("directory path({directory}) doesn't exist".format(directory=self.__directory))
        if not os.path.isdir(self.__directory):
            raise Exception("directory path({directory}) is not a directory".format(directory=self.__directory))
        file_path = os.path.join(self.__directory, self.__filename)
        if not os.path.exists(file_path):
            raise Exception("file path({file_path}) doesn't exist".format(file_path=file_path))
        if not os.path.isfile(file_path):
            raise Exception("file path({file_path}) is not a file".format(file_path=file_path))

    def __check_export_file_type(self, file_path: str,
                                datetime_pattern_dict = __kakaotalk_datetime_pattern_dict):
        with open(file_path, 'r', encoding = 'utf-8') as f:
            for counter in range(5):
                line = f.readline()
                if not line: break

                for file_type, pattern in datetime_pattern_dict.items():
                    if re.search(pattern, line):
                        return '_'.join(file_type.split('_')[:2])
        
        print("Error: Cannot know the device type and language of the file.\n",
            f"Please check the file is a kakaotalk export file or the export enviroment is in among {str(list(kakaotalk_include_date_pattern_dict.keys()))}")

    def __parse(self, file_type: str, file_path, datetime_pattern_dict=__kakaotalk_datetime_pattern_dict):
        msgs = []
        if file_type == 'window_ko':     # window
            date_pattern = datetime_pattern_dict['window_ko_date']
            time_pattern = datetime_pattern_dict['window_ko_time']

            with open(file_path) as file: 
                # 줄바꿈되어있는 경우도 묶어주기 위해 buffer 사용
                buffer = ''
                date = ''

                for line in file:
                    # window파일의 데이트str(--------------- 2020년 6월 28일 일요일 ---------------)이거나 시간 str([김한길] [오후 2:15] htt)이면
                    if re.match(date_pattern, line) or re.match(time_pattern, line):
                        # buffer가 time_pattern으로 시작하는 경우만 추가해주기
                        if re.match(time_pattern, buffer):  
                            buffer_tokens = buffer.split(']', maxsplit=2)
                            user_name = buffer_tokens[0].replace('[', '').strip()
                            time = buffer_tokens[1].replace('[', '').strip()
                            my_datetime = self.__str_to_datetime(file_type, f"{date} {time}")
                            text = buffer_tokens[2].strip()
                            
                            msgs.append({'datetime': my_datetime,
                                            'user_name': user_name,
                                            'text': text
                            })

                        if re.match(date_pattern, line):  # window파일의 데이트str이면
                            date = line.replace('-', '').strip().rsplit(" ", 1)[0]
                            buffer = ''
                        else:  #  window파일의 시간 str이면
                            buffer = line

                    else:
                        buffer += line

        else: # android
            datetime_pattern = datetime_pattern_dict[file_type]
            msg_exist_check_pattern = datetime_pattern + ",.*:"
            
            with open(file_path) as file: 
                # 줄바꿈되어있는 경우도 저장하기 위해 buffer 사용
                buffer=''
                for line in file:
                    if re.match(datetime_pattern, line):
                        if re.match(msg_exist_check_pattern, buffer):
                            
                            temp_01_2_tokens = buffer.split(" : ", maxsplit=1)
                            temp_0_1_tokens = temp_01_2_tokens[0].rsplit(",", maxsplit=1)

                            my_datetime = temp_0_1_tokens[0].strip()
                            my_datetime = self.__str_to_datetime(file_type, my_datetime)
                            user_name = temp_0_1_tokens[1].strip()
                            text = temp_01_2_tokens[1].strip()
                            msgs.append({'datetime': my_datetime,
                                        'user_name': user_name,
                                        'text': text
                            })

                        buffer = line
                    else:
                        buffer += line
        
        return msgs
    

    def __str_to_datetime(self, file_type, text):
        kakaotalk_strptime_pattern_dict = {'ko': '%Y년 %m월 %d일 %p %I:%M',
                                            'en': '%B %d, %Y at %I:%M %p',
                                            }

        os_type, language = file_type.split('_')
        if language == 'ko':
            text = text.replace('오전', 'AM')
            text = text.replace('오후', 'PM')

        text_dt = datetime.strptime(text, kakaotalk_strptime_pattern_dict[language])
        return text_dt

if __name__ == "__main__":
    reader = MessageReader(".", "android_en.txt")

    for msg in reader.get_messages():
        print(msg)
