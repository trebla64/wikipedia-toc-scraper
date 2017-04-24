# wikipedia-toc-scraper
Web application that uses the Pyramid framework to scrape table of contents of Wikipedia pages

# Installation

To install the project it is best to create a virtual environment for Python, and then use that environment
to install/run the project in.

To create the environment, use:
```
$ python -m venv <env_path>
```
where <env_path> is the the path to your virtual environment directory.

After the environment has been set up, clone the repository into a directory, change into that directory and
run:
```
$ <env_path>/Scripts/pip install -r requirements.txt -e .
```

This will install the list of requirements needed to test/run the project.

# Testing

The tests can be run with:
```
$ <env_path>/Scripts/pytest
```

# Running

To run the project, execute the following command:
```
$ <env_path>/Scripts/pserve development.ini
```

This should start up the server, which can be accessed through the browser on localhost, port 6543.

# How the project was created

The commands used to create the project was (on Windows):
```
> set VENV=c:\virtualenvs\wikipedia-toc-scraper
> python -m venv %VENV%
> %VENV%\Scripts\pip install "pyramid==1.8.3"
> %VENV%\Scripts\pip install cookiecutter
> cd C:\Repos\
> %VENV%\Scripts\cookiecutter https://github.com/Pylons/pyramid-cookiecutter-starter

   project_name = wikipedia-toc-scraper
   repo_name = wikipedia_toc_scraper
   template_language = 1

> cd wikipedia_toc_scraper
> %VENV%\Scripts\pip install -e ".[testing]"
> %VENV%\Scripts\pip freeze >requirements.txt
```

