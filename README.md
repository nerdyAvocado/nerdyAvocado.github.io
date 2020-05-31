# nerdyAvocado.github.io

## Workflow
### Pre-commit
To activate the pre-commit hook on your local clone of the repo, run the following command from the top-level of the checkout:
`chmod +x generate_tag_index.py`
`cp pre-commit .git/hooks/pre-commit`

You may need to change the python shebag line in `generate_tag_index.py` to point at the correct oython command, if the alias python3 is not setup in your dev environment.