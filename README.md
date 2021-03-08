<p align="center">
<a href="https://github.com/starship/starship">Starship</a> cross-shell prompt in xonsh shell.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20prompt%20for%20the%20xonsh%20shell!&url=https://github.com/anki-code/xontrib-xontrib-prompt-starship" target="_blank">tweet</a>.
</p>


## Installation

To install use pip:

```bash
xpip install xontrib-prompt-starship
# or: xpip install -U git+https://github.com/anki-code/xontrib-prompt-starship
```

## Usage

```bash
xontrib load prompt_starship
```

## Recommendation

We suggest to use `@` character to remember about you're using xonsh syntax and to potentially spread the word about xonsh if you make a screenshot or show your terminal to friends or collegues. Add this to your `~/.config/starship.toml`:
```ini
[character]
success_symbol = "[@](bold green)"
error_symbol = "[@](bold red)"
```
If you're using Starship for both for another shell and for xonsh and you want to have different characters you can just put the lines above to the new `~/.config/starship_xonsh.toml` file. Then you should add to the `~/.xonshrc` file the line `$STARSHIP_CONFIG = '~/.config/starship_xonsh.toml'` before `xontrib load prompt_starship`.

## Credits
* This package is the part of [ergopack](https://github.com/anki-code/xontrib-ergopack) - the pack of ergonomic xontribs.
* This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
