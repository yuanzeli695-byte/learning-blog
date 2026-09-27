# 先写入第一行，再用 a 模式追加第二行。
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    file = Path(folder) / 'note.txt'
    file.write_text('第一行\n', encoding='utf-8')
    with file.open('a', encoding='utf-8') as stream:
        stream.write('第二行\n')
    print(file.read_text(encoding='utf-8'))
