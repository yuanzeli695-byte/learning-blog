# 整个示例都在临时目录，不碰个人数据文件。
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    original = Path(folder) / 'note.txt'
    temporary = Path(folder) / 'note.new.txt'
    original.write_text('一天学一点\n', encoding='utf-8')
    text = original.read_text(encoding='utf-8')
    temporary.write_text(text.replace('一天', '一年'), encoding='utf-8')
    temporary.replace(original)
    print(original.read_text(encoding='utf-8'))
