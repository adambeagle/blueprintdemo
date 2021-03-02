This repo contains two demonstration Flask applications for use with this presentation on Flask blueprints: https://docs.google.com/presentation/d/1N0DClCOH4Dr9Nke7Zx9HZ7_cdyMOIjZWRMOVhl89u1Y/edit?usp=sharing

The applications are equivalent in terms of end user experience, but are structured differently. The `blueprint` application is a refactored version of `monolith`, making use of blueprints and the application factory pattern.

Both applications have the same requirements, so one virtual environment may be used for both. Both also use the default flask_sqlalchemy database &mdash; a temporary sqllite file.

To run either application use `flask run` inside the application root directory (`monolith` or `blueprint`).
