# TemporaryDirectory 会在结束后清理练习文件。
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    file = Path(folder) / 'note.txt'
    file.write_text('第一行\n第二行\n', encoding='utf-8')
    with file.open('r', encoding='utf-8') as stream:
        print(stream.read())
