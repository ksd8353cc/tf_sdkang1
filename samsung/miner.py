from konlpy.tag import Okt
import re
from nltk.tokenize import word_tokenize

class Samsung:
    def __init__(self):
        okt = Okt()
        okt.pos("삼성전자 글로벌 센터 전자사업부", stem=True)
        filename = './data/kr-Report_2018.txt'
        with open(filename, 'r', encoding='utf-8') as f:
            texts = f.read()


    @staticmethod
    def extract_hangeul(texts):
        texts = texts.replace('\n', ' ')  # 해당줄의 줄바꿈 내용 제거
        tokenizer = re.compile(r'[^ ㄱ-힣]+')  # 한글과 띄어쓰기를 제외한 모든 글자를 선택
        texts = tokenizer.sub('', texts)  # 한글과 띄어쓰기를 제외한 모든 부분을 제거
        return text

    @staticmethod
    def change_token(texts):
        tokens = word_tokenize()
        print(tokens[:7])
