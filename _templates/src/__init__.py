import datetime


name = "<<name>>"
package_name = "<<package-name>>"
author = "<<author>>"
author_email = "<<email>>"
description = "<<description>>"
url = "<<url>>"
<<requires::packaging
project_urls = {
    <<requires::docs "Documentation": f"https://automl.github.io/<<package-name>>/main" endrequires::docs>>,
    "Source Code": f"https://github.com/automl/<<package-name>>",
}
endrequires::packaging>>
copyright = f"Copyright {datetime.date.today().strftime('%Y')}, AutoML.org Freiburg-Hannover"
version = "0.0.1"
