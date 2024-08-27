# InstaTips


#### Setup a virtual python environment
* Must have pyenv installed and know how to use it, check this [tutorial](https://blog.teclado.com/how-to-use-pyenv-manage-python-versions/)
* Execute the following commands on the terminal in this folder
```
pyenv local 3.11
pyenv exec python -v
cd ..
pyenv exec python -v venv .venv
source .venv/bin/activate
```

#### Install the projet packages
```
cd ..
pip install -r requirements.txt
```

#### Python code formating, linting and sorting imports with ruff
* Use the following settings as the VSCode workspace (project level) settings to enable ruff's automatic linting, formating and sortins of imports.
```
{
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit",
            "source.fixAll": "explicit"
        }
    },
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "charliermarsh.ruff"
}
```
#### Launch the application
* After activating the python virtual environment to work on the projet, you can launch the application using this command:
```
uvicorn api.main:app --reload
```
