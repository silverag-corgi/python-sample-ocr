import os
import sys
from types import ModuleType

import pyocr
from PIL import Image
from pyocr import tesseract
from pyocr.builders import TextBuilder

if __name__ == '__main__':
    # pipenv run py -m src.main
    
    # 環境変数の設定
    TESSERACT_PATH: str = 'C:\\Program Files\\Tesseract-OCR'
    TESSDATA_PATH:  str = 'C:\\Program Files\\Tesseract-OCR\\tessdata'
    os.environ['PATH'] += os.pathsep + TESSERACT_PATH
    os.environ['TESSDATA_PREFIX'] = TESSDATA_PATH

    # OCRツールの取得
    tools: list[ModuleType] = pyocr.get_available_tools()
    if len(tools) == 0:
        print('OCRツールが見つかりません。')
        sys.exit(1)
    tool: ModuleType = tools[0]

    # 画像の読み込み
    image: Image.Image = Image.open('./pic/item_list_01.png')

    # ビルダーの設定
    builder: TextBuilder = TextBuilder(tesseract_layout=6)

    # 画像から文字列への変換
    image_text: str = tool.image_to_string(image , lang='jpn', builder=builder)
    # image_text: str = tesseract.image_to_string(image , lang='jpn', builder=builder)

    # 半角スペースの削除
    image_text = image_text.replace(' ', '')

    print(image_text)
