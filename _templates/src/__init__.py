name = "<<name>>"
package_name = "<<package-name>>"
author = "<<author>>"
author_email = "<<email>>"
description = "<<description>>"
url = "<<url>>"
<<requires::packaging
project_urls = {
    <<requires::docs "Documentation": f"https://automl.github.io/{package_name}/main" endrequires::docs>>,
    "Source Code": f"https://github.com/automl/{package_name}",
}
endrequires::packaging>>
version = "0.0.1"
