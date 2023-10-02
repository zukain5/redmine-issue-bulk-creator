# redmine-issue-bulk-creator
A CLI tool to register issues in redmine at specified intervals.

## Installation
The Python package manager [rye](https://github.com/mitsuhiko/rye) is used for this repository.
Clone this repository and run the following command.

```shell
rye sync
```

## Configuration
The redmine URL and API key are required for execution.
Create an .env file in the project root and register the URL and API key.

```shell
touch .env
echo "REDMINE_URL=https://redmine.example.com" >> .env
echo "REDMINE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxx" >> .env
```

## Usage
```shell
rye run src/main.py
```
A few questions will be asked, and at the end issues will be registered in redmine.
