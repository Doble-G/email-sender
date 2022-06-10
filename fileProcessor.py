from dataclasses import dataclass
import json
import logging

@dataclass
class FileProcessor:
    """
    This class is used to process files.
    """
    path:str
    file_name: str

    def is_empty(self)->bool:
        """
        This function is used to check if the file is empty.
        :return: True if the file is empty, False otherwise
        """
        try:
            with open( self.path + self.file_name, 'r') as file:
                return file.read() == ''
        except FileNotFoundError as e:
            logging.error("Error oppening file "+self.path + self.file_name+" error: "+str(e))
            return True

    def get_file_content_json(self)->json:
        """
        This function is used to get the file content.
        :return: the file content
        """
        with open(  self.path + self.file_name, 'r') as file:
            for line in file:
                try:
                    yield json.loads(line)
                except json.decoder.JSONDecodeError:
                    yield {}
                
    def delete_lines(self, lines: list)->bool:
        """
        This function is used to delete lines from a file.
        :param lines: the list of lines to delete
        :return: True if the lines were deleted successfully, False otherwise
        """
        try:
            with open(  self.path + self.file_name, 'r') as file:
                lines_as_json = [json.loads(line) for line in file]
                lines_to_keep=[]
                for line in lines_as_json:
                    if line not in lines:
                        lines_to_keep.append(line)
                with open(  self.path + self.file_name, 'w') as file:
                    for line in lines_to_keep:
                        file.write(json.dumps(line) + '\n')
            return True
        except FileNotFoundError as e:
            logging.error("Error oppening file "+self.path + self.file_name+" error: "+str(e))
            return False
