__xonsh__.env['STARSHIP_SHELL'] = 'sh'  # Fix https://github.com/anki-code/xontrib-prompt-starship/issues/1
__xonsh__.env['PROMPT'] = lambda: __xonsh__.subproc_captured_stdout([
    'starship', 'prompt',
    '--status', str(__xonsh__.history[-1].rtn) if len(__xonsh__.history) > 0 else '0',
    '--cmd-duration', str(int((__xonsh__.history[-1].ts[1] - __xonsh__.history[-1].ts[0])*1000)) if len(__xonsh__.history) > 0 else '0',
    '--jobs', str(len(__xonsh__.all_jobs))
])
