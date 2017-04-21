# wikipedia-toc-scraper
Web application that uses the Pyramid framework to scrape table of contents of Wikipedia pages

# Installation

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

# Testing/Running

