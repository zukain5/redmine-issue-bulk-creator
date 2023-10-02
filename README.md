# redmine-issue-bulk-creator
A CLI tool to register issues in redmine at specified intervals.

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
