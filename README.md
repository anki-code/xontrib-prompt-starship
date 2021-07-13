<p align="center">
<a href="https://github.com/starship/starship">Starship</a> cross-shell prompt in xonsh shell.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20prompt%20for%20the%20xonsh%20shell!&url=https://github.com/anki-code/xontrib-xontrib-prompt-starship" target="_blank">tweet</a>.
</p>

Additional features:

* You can split the prompt to left, right and bottom parts.

## Installation

To install use pip:

```bash
# You already have Starship installed. Then:
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
If you're using Starship for both for another shell and for xonsh and you want to have different characters you can just put the lines above to the new `~/.config/starship_xonsh.toml` file. Then you should add to the `~/.xonshrc`: 

```python
$STARSHIP_CONFIG = '~/.config/starship_xonsh.toml'
xontrib load prompt_starship
```

## Configuration

You can set the different starship configs for left, right and bottom parts of prompt when your shell type is prompt-toolkit:

```python
$XONTRIB_PROMPT_STARSHIP_LEFT_CONFIG = "~/.config/starship_xonsh_left.toml"
$XONTRIB_PROMPT_STARSHIP_RIGHT_CONFIG = "~/.config/starship_xonsh_right.toml"
$XONTRIB_PROMPT_STARSHIP_BOTTOM_CONFIG = "~/.config/starship_xonsh_bottom.toml"
xontrib load prompt_starship
```

In case of [using starship as part of another prompt](https://github.com/anki-code/xontrib-prompt-bar#using-starship-cross-shell-prompt-to-rendering-right-sections) you can add starship prompt to `$PROMPT_FIELDS` without replacing the current prompt:
```python
$XONTRIB_PROMPT_STARSHIP_REPLACE_PROMPT = False
xontrib load prompt_starship
print($PROMPT_FIELDS['starship_left']())
```

## Known issues

* [Prompt toolkit issue: the right prompt at the bottom.](https://github.com/prompt-toolkit/python-prompt-toolkit/issues/1241)
* The using of bottom toolbar is not properly tested and adopted to cute appearance.

## Credits
* The xontrib-prompt-starship can be used as part of [xontrib-prompt-bar](https://github.com/anki-code/xontrib-prompt-bar).
* This package is the part of [ergopack](https://github.com/anki-code/xontrib-ergopack) - the pack of ergonomic xontribs.
* This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
* [Adding support for xonsh inside Starship](https://github.com/starship/starship/pull/2807)
