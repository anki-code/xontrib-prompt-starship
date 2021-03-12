import sys
from pathlib import Path


__xonsh__.env['STARSHIP_SHELL'] = 'sh'  # Fix https://github.com/anki-code/xontrib-prompt-starship/issues/1
__xonsh__.env['STARSHIP_SESSION_KEY'] = __xonsh__.subproc_captured_stdout(['starship','session']).strip()


def _starship_prompt(cfg=None):
    cmd = [
        'starship', 'prompt',
        '--status', str(int( __xonsh__.history[-1].rtn)) if len(__xonsh__.history) > 0 else '0',
        '--cmd-duration' , str(int((__xonsh__.history[-1].ts[1] - __xonsh__.history[-1].ts[0])*1000)) if len(__xonsh__.history) > 0 else '0',
        '--jobs', str(len(__xonsh__.all_jobs))
    ]

    env = {'STARSHIP_CONFIG': cfg} if cfg else {}
    with __xonsh__.env.swap(env):
        return __xonsh__.subproc_captured_stdout(cmd)

        
_left_cfg  = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_LEFT' , '')
_left_cfg = Path(_left_cfg).expanduser() if _left_cfg else _left_cfg

if _left_cfg and not _left_cfg.exists():
    print(f"xontrib-prompt-starship: The path doesn't exist: {_left_cfg}", file=sys.stderr)

__xonsh__.env['PROMPT']	= lambda: _starship_prompt(_left_cfg)


_right_cfg = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_RIGHT', '')
_right_cfg = Path(_right_cfg ).expanduser() if _right_cfg else _right_cfg 
if _right_cfg:
    if _right_cfg.exists():
        __xonsh__.env['RIGHT_PROMPT'] = lambda: _starship_prompt(_right_cfg)
    else:
        print(f"xontrib-prompt-starship: The path doesn't exist: {_right_cfg}", file=sys.stderr)
