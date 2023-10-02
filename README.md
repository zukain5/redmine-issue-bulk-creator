# redmine-issue-bulk-creator
A CLI tool to register issues in redmine at specified intervals.

## Installation
The Python package manager [rye](https://github.com/mitsuhiko/rye) is used for this repository.
Clone this repository and run the following command.
If you do not have rye installed, install it first.

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

## Example
```shell
$ rye run python src/main.py
? What is the issue subject? test
? When is the start date? (write in a format like 1970-01-01) 2023-01-01
? How many days is the interval? 5
? How many days until the deadline? 2
? Which project? project-name
? How many issues do you want to create? 5
Created: \#959 test  # 2023-01-01 ~ 2023-01-02
Created: \#960 test  # 2023-01-06 ~ 2023-01-07
Created: \#961 test  # 2023-01-11 ~ 2023-01-12
Created: \#962 test  # 2023-01-16 ~ 2023-01-17
Created: \#963 test  # 2023-01-21 ~ 2023-01-22
Created all issues.
```
