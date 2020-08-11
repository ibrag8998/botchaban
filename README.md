# Chaban

Python chat-bot framework. Uses very much concepts from [django](https://github.com/django/django/).

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

To bootstrap a new project, I recommend using [cookiecutter](https://github.com/cookiecutter/cookiecutter).

```shell
pip install cookiecutter
```

For now, CLI is not developed, but I hope it will be available soon.

Now, run this command to get your chaban template:

```shell
cookiecutter gh:ibrag8998/cookiecutter-chaban
```

And answer to the question it asks :D.

The project looks like this:

```
project_slug
+-- project_slug
|   +-- __init__.py
|   +-- handlers.py
|   +-- actions.py
|   +-- text.py
+-- settings
|   +-- __init__.py
|   +-- base.py
|   +-- dev.py
+-- requirements
|   +-- base.txt
|   +-- testing.txt
|   +-- local.txt
+-- scripts
|   +-- installdeps.sh
|   +-- mkenv.sh
+-- run.py
+-- ...
```

Now run `mkenv.sh` script to make `.env` file which stores some configuration and secret keys:

```shell
cd scripts
./mkenv.sh
```

- `settings/` contains any settings you want, but there some required ones, like `DEBUG`.
Put base settings in `base.py` and development-only ones in `dev.py`, the rest will be done for you.
How? Read `settings/__init__.py` file.

- `requirements/` contains separate requirements. `base.txt` are base, project will not work
without them. `testing.txt` only used for tests. `local.txt` contains requirements for direct developer,
for example: linter, formatter.

- `scripts/` contains bash scripts to manage your project.

- `run.py` is a file that you will run to start up your bot.

- `project_slug/` is actual core:

  - `handlers.py` contains message handlers.
  - `actions.py` contains logic that will be invoked by message handler.
  - `text.py` contains text snippet to send in messages.

### Settings and config

### Actual code

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

## Contributing

Please, help.
