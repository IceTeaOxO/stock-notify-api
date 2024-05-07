import json
import os
from dotenv import load_dotenv


class FileManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileManager, cls).__new__(cls)
            # 在這裡初始化 ThreadManager 的屬性
        return cls._instance

    def __init__(self):
        load_dotenv()
        self.directory = os.getenv('file_directory')
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def create_json_file(self, file_name):
        """创建一个空的JSON文件"""
        path = os.path.join(self.directory, f"{file_name}.json")
        with open(path, 'w') as file:
            json.dump({}, file)
        print(f"File '{file_name}.json' created successfully.")

    def read_json_file(self, file_name):
        """读取并返回JSON文件的内容"""
        path = os.path.join(self.directory, f"{file_name}.json")
        try:
            with open(path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File '{file_name}.json' not found.")
            return None

    def write_json_to_file(self, json_data, file_name):
        """将JSON数据写入指定的文件中"""
        self.create_json_file(file_name)
        path = os.path.join(self.directory, f"{file_name}.json")
        with open(path, 'w') as file:
            json.dump(json_data, file, indent=4)
        print(f"Data written to '{file_name}.json' successfully.")
