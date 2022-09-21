let s:save_cpo = &cpo
set cpo&vim

py3file <sfile>:h:h/python3/test.py
python3 import vim

function! passgen#passgen(size)
  python3 vim.command("call setline('.', '%s')" % test(vim.eval('a:size')))
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo
