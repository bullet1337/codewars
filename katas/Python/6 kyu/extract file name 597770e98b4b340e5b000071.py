# https://www.codewars.com/kata/597770e98b4b340e5b000071
import re


pattern = re.compile(r'\d+_(\S+)\.')

class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        return pattern.match(dirty_file_name).group(1)