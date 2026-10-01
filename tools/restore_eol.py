# 恢复换行符：未改动的行沿用 HEAD 里原来的 CRLF/LF，新行跟随上一行原来的换行符。
# 用法：python3 restore_eol.py <repo> <file> [<file> ...]（基准为该仓库 HEAD）
import subprocess, difflib, sys
repo = sys.argv[1]
for path in sys.argv[2:]:
    r = subprocess.run(['git', '-C', repo, 'show', f'HEAD:{path}'], capture_output=True)
    if r.returncode != 0:
        continue
    orig = r.stdout.decode('utf-8')
    full = f'{repo}/{path}'
    new = open(full, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    ol = orig.splitlines(keepends=True); ok = [l.rstrip('\r\n') for l in ol]
    nl = new.split('\n'); trailing = new.endswith('\n')
    if trailing: nl = nl[:-1]
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ok, nl, autojunk=False).get_opcodes():
        if tag == 'equal': out.extend(ol[i1:i2])
        else:
            ref = ol[i1-1] if i1 > 0 else (ol[0] if ol else '\n')
            end = '\r\n' if ref.endswith('\r\n') else '\n'
            out.extend(l + end for l in nl[j1:j2])
    open(full, 'w', encoding='utf-8', newline='').write(''.join(out))
