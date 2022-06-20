import sys
from pathlib import Path


__xonsh__.env['STARSHIP_SHELL'] = 'xonsh'
__xonsh__.env['STARSHIP_SESSION_KEY'] = __xonsh__.subproc_captured_stdout(['starship','session']).strip()


def _starship_prompt(cfg=None):
    with __xonsh__.env.swap({'STARSHIP_CONFIG': cfg} if cfg else {}):
        return __xonsh__.subproc_captured_stdout([
            'starship', 'prompt',
            '--status', str(int( __xonsh__.history[-1].rtn)) if len(__xonsh__.history) > 0 else '0',
            '--cmd-duration' , str(int((__xonsh__.history[-1].ts[1] - __xonsh__.history[-1].ts[0])*1000)) if len(__xonsh__.history) > 0 else '0',
            '--jobs', str(len(__xonsh__.all_jobs))
        ])

    
_replace = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_REPLACE_PROMPT' , True)
    
    
_left_cfg  = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_LEFT_CONFIG' , '')
_left_cfg = Path(_left_cfg).expanduser() if _left_cfg else _left_cfg
if _left_cfg and not _left_cfg.exists():
    print(f"xontrib-prompt-starship: The path doesn't exist: {_left_cfg}", file=sys.stderr)

__xonsh__.env['PROMPT_FIELDS']['starship_left']	= lambda: _starship_prompt(_left_cfg)
if _replace:
    __xonsh__.env['PROMPT'] = '{starship_left}'


_right_cfg = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_RIGHT_CONFIG', '')
_right_cfg = Path(_right_cfg).expanduser() if _right_cfg else _right_cfg 
if _right_cfg:
    if _right_cfg.exists():
        __xonsh__.env['PROMPT_FIELDS']['starship_right'] = lambda: _starship_prompt(_right_cfg)
        if _replace:
            __xonsh__.env['RIGHT_PROMPT'] = '{starship_right}'
    else:
        print(f"xontrib-prompt-starship: The path doesn't exist: {_right_cfg}", file=sys.stderr)

        
_bottom_cfg = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_BOTTOM_CONFIG', '')
_bottom_cfg = Path(_bottom_cfg).expanduser() if _bottom_cfg else _bottom_cfg 
if _bottom_cfg:
    if _bottom_cfg.exists():
        __xonsh__.env['PROMPT_FIELDS']['starship_bottom_toolbar'] = lambda: _starship_prompt(_bottom_cfg)
        if _replace:
            __xonsh__.env['BOTTOM_TOOLBAR'] = '{starship_bottom_toolbar}'
    else:
        print(f"xontrib-prompt-starship: The path doesn't exist: {_bottom_cfg}", file=sys.stderr)
