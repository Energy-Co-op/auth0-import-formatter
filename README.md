# auth0-import-formatter
Auth0 Import Formatter application for transforming an Excel spreadsheet containing memmber information to a JSON format compatible with the Auth0 user import tool.

## See:
* https://auth0.com/docs/manage-users/user-migration/bulk-user-import-export
* https://auth0.com/docs/manage-users/user-migration/bulk-user-import-database-schema-and-examples

## Requirements
* [Python](https://www.python.org/downloads/) 3.14 or greater

## Install dependencies
```bash
py -m pip install .
```

## Build
```bash
py -m build
```

# Run
1. Change variables in `config.ini` for the file to be read in
2. Run
```bash
py ./app.py
```
3. Provide the filename for the spreadsheet to import and format to JSON
4. See the output in `out.json`
