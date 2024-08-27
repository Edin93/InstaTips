## InstaTips

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

