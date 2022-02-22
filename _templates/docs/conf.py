import automl_sphinx_theme

from <<package-name>> import copyright, author, version, name


options = {
    "copyright": copyright,
    "author": author,
    "version": version,
    "name": name,
    "html_theme_options": {
        "github_url": "https://automl.github.io/<<name>>/main"
        # "twitter_url": "https://automl.github.io/<<name>>/main"
    }
}

automl_sphinx_theme.set_options(globals(), options)
