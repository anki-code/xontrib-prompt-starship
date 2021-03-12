from os import path

_starship_cfg_left  = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_LEFT' , '')
_starship_cfg_right = __xonsh__.env.get('XONTRIB_PROMPT_STARSHIP_RIGHT', '')

__xonsh__.env['STARSHIP_SHELL'] = 'sh'  # Fix https://github.com/anki-code/xontrib-prompt-starship/issues/1
__xonsh__.env['STARSHIP_SESSION_KEY'] = __xonsh__.subproc_captured_stdout(['starship','session']).strip()

def _starship_prompt():
  return __xonsh__.subproc_captured_stdout([
    'starship', 'prompt',
    '--status'       , str(int( __xonsh__.history[-1].rtn))\
      if len(__xonsh__.history) > 0 else '0',
    '--cmd-duration' , str(int((__xonsh__.history[-1].ts[1] - __xonsh__.history[-1].ts[0])*1000))\
      if len(__xonsh__.history) > 0 else '0',
    '--jobs', str(len(__xonsh__.all_jobs))
    ])

def _starship_prompt_left():
  if _starship_cfg_left:
    with __xonsh__.env.swap(STARSHIP_CONFIG=_starship_cfg_left):
      return _starship_prompt()
  else:
    return _starship_prompt()
__xonsh__.env['PROMPT']	= _starship_prompt_left

if path.exists(_starship_cfg_right):
  def _starship_prompt_right():
    with __xonsh__.env.swap(STARSHIP_CONFIG=_starship_cfg_right):
      return _starship_prompt()
  __xonsh__.env['RIGHT_PROMPT']	= _starship_prompt_right
