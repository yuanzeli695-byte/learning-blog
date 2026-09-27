# 我把读写限制在临时目录，不依赖私人 data 文件。
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    file = Path(folder) / 'note.txt'
    file.write_text('第一行\n第二行\n', encoding='utf-8')
    with file.open('r', encoding='utf-8') as stream:
        print(stream.read())
