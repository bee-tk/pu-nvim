let s:save_cpo = &cpo
set cpo&vim

py3file <sfile>:h:h/python3/test.py
python3 import vim

function! test#test()
  python3 test()
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo
