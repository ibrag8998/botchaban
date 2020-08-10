# Chaban

Python chat-bot framework.

## Links

- [PyPI](https://pypi.org/project/chaban/)
- [GitHub](https://github.com/ibrag8998/chaban/)

## Current state

Under heavy development. Chaban supposed to be framework for developing bots for many platforms.
Now working on telegram bots. Also this project needs to have strong CLI, which is also in development.

## Installation

```shell
pip install chaban
```

## Usage

### Project structure

For now, CLI is not developed, so you need to make projects by yourself :(.
Recommended project structure:

```
project_name
+-- project_name
|   +-- __init__.py
|   +-- handlers.py
|   +-- actions.py
+-- settings
|   +-- __init__.py (only this one required, others are optional)
|   +-- base.py
|   +-- ...
+-- run.py
+-- .env (recommended)
```

### Settings and config

In your settings, you just need to specify `TELEGRAM_TOKEN: str` like this:

```python
TELEGRAM_TOKEN = ...  # your token here, recommended to store it in env variable
```

Also, you need to specify `PACKAGES: List[str]`. For the project structure you can see above,
this setting should look like this:

```python
PACKAGES = [
    'project_name',
]
```

### Actual code

In your nested `project_name/` dir, you can see `handlers.py` and `actions.py`.
First, define a message handler in `handlers.py` like this:

```python
from chaban.handlers import CommandMH

class StartCommandMH(CommandMH):
    command = 'start'
```

Now, when a message comes, and your handler looks like the message can be handled by it
(checked by using regex, more info in source code), the `action` will be called. But wait.
We didn't define any action! Head over to `actions.py` and add one:

```python
from chaban.actions import Action

class StartCommandAction(Action):
    def act(self, message: dict) -> None:
        self.tbot.send_message(message['chat']['id'], 'Welcome!')
```

Well, action is defined, now let's link the handler with the action.
Open `handlers.py` file and action attribute like this:

```python
...
from .actions import StartCommandAction

class StartCommandMH(CommandMH):
    ...
    action = StartCommandAction()
```

That's all for basics :D. Now open up your terminal and start bot:

```shell
python run.py
```

Write to your bot with message "**/start**" and see it works.

### Note

The CLI will be available soon (I hope) and the project organization will be much easier.

## Contributing

Please, help.
