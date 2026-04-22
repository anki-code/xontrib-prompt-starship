"""Starship cross-shell prompt in xonsh shell. """

import sys as _sys
from pathlib import Path as _Path


__xonsh__.env['STARSHIP_SHELL'] = 'xonsh'
__xonsh__.env['STARSHIP_SESSION_KEY'] = __xonsh__.subproc_captured_stdout(['starship','session']).strip()


def _starship_prompt(cfg: str) -> None:
    import os
    hist = __xonsh__.history
    if len(hist) > 0:
        rtn = hist[-1].rtn
        status = str(int(rtn)) if rtn is not None else '0'
        ts = hist[-1].ts
        duration = str(int((ts[1] - ts[0]) * 1000)) if ts[1] is not None else '0'
    else:
        status = '0'
        duration = '0'
    with __xonsh__.env.swap({'STARSHIP_CONFIG': cfg} if cfg else {}):
        return __xonsh__.subproc_captured_stdout([
            'starship', 'prompt',
            '--status=' + status,
            '--cmd-duration', duration,
            '--jobs', str(len([j for j in __xonsh__.all_jobs.values() if j['pids']])),
            '--terminal-width', str(os.get_terminal_size().columns),
        ])


_replace = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_REPLACE_PROMPT' , True)


_left_cfg  = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_LEFT_CONFIG' , __xonsh__.env.get('STARSHIP_CONFIG' , ''))
if _left_cfg:
    _left_cfg = _Path(_left_cfg).expanduser()
    if not _left_cfg.exists():
        print(f"xontrib-prompt-starship: The path doesn't exist: {_left_cfg}", file=_sys.stderr)

__xonsh__.env['PROMPT_FIELDS']['starship_left']	= lambda: _starship_prompt(_left_cfg)
if _replace:
    __xonsh__.env['PROMPT'] = '{starship_left}'


_right_cfg = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_RIGHT_CONFIG', '')
if _right_cfg:
    _right_cfg = _Path(_right_cfg).expanduser()
    if _right_cfg.exists():
        __xonsh__.env['PROMPT_FIELDS']['starship_right'] = lambda: _starship_prompt(_right_cfg)
        if _replace:
            __xonsh__.env['RIGHT_PROMPT'] = '{starship_right}'
    else:
        print(f"xontrib-prompt-starship: The path doesn't exist: {_right_cfg}", file=_sys.stderr)


_bottom_cfg = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_BOTTOM_CONFIG', '')
if _bottom_cfg:
    _bottom_cfg = _Path(_bottom_cfg).expanduser()
    if _bottom_cfg.exists():
        __xonsh__.env['PROMPT_FIELDS']['starship_bottom_toolbar'] = lambda: _starship_prompt(_bottom_cfg)
        if _replace:
            __xonsh__.env['BOTTOM_TOOLBAR'] = '{starship_bottom_toolbar}'
    else:
        print(f"xontrib-prompt-starship: The path doesn't exist: {_bottom_cfg}", file=_sys.stderr)
