# Project structure
Desktop application for managing images of the studies.
<pre>
app-image-desktop/
│
├── bin/
│
├── docs/
│   └── appImageDesktop.md
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   └── config.yml
│   │ 
│   ├── templates/
│   │   ├── __init__.py
│   │   ├── main.ui
│   │   └── check_image.ui
│   │ 
│   ├── applicaciton/
│   │   ├── __init__.py
│   │   ├── use_case
│   │   └── controller
│   │
│   ├── dominio/
│   │   ├── __init__.py
│   │   ├── entity
│   │   │   ├── __init__.py
│   │   │   └── image.py
│   │   ├── exception
│   │   ├── value_object
│   │   ├── services
│   │   └── respository
│   │
│   ├── infrastucture/
│   │   ├── __init__.py
│   │   ├── entity
│   │   ├── value_object
│   │   ├── services
│   │   └── respository
│   └──   
│
├── tests/
│   ├──applicaciton
│   │   ├── helpers_tests.py
│   │   └── hello_tests.py
│   │
│   ├── dominio/
│   │   ├── helpers_tests.py
│   │   └── hello_tests.py
│   │
│   └── infrastucture/
│       ├── helpers_tests.py
│       └── world_tests.py
│
├── .gitignore
├── LICENSE
├── requeriments.txt
├── README.md
└── setup.py
</pre>

# Run Application

Option 1) 

If you use PyCharm, simply open the file setup.py, and PyCharm will ask you to install the dependencies, it answers yes, and then with the Run -> Run or the Run button you will be able to execute the application.
www.jetbrains.com/pycharm/download/

Option 2)

First application dependency:
```python
python -m pip install -r requirements.txt
```
Execute application:
```python
python3 app/main.py
```

For use this application is necessary the api:
```
https://github.com/acostasg/app-image-api
```

# Create Executable Application
```python
pyinstaller --onefile --windowed main.py
```

#TODO
- autoupdate application
