## FastAPI Template using the Repository Pattern Approach

This project is a backend template for a FastAPI-based application that uses the repository pattern approach to provide an abstraction layer between the business logic and the data access layer. It aims to provide a scalable and maintainable architecture for building web applications.


## Features

✅ Quick and easy setup: just execute Cookiecutter and set the input variables in minutes.

✅ Setup takes only 30 seconds, getting you up and running quickly.

✅ First entity with CRUD endpoints already developed, saving you time and effort.

✅ 100% test coverage included, so you can ensure your code works as expected.

✅ Repository pattern design leverages [Redbird](https://github.com/Miksus/red-bird) implementation, supporting both NoSql and SQL repositories

✅ [Poetry](https://python-poetry.org/) used for package management, simplifying dependency management.

✅ [Dependency Injector](https://python-dependency-injector.ets-labs.org/) included for easy service and repository injection, reducing boilerplate code.

✅ [ruff](https://beta.ruff.rs/docs/) and [black](https://github.com/psf/black) used for linting, ensuring consistent and clean code.

✅ Consistent structure with pre-defined naming conventions, making it easy to navigate your codebase.


### Getting Started

To use this template, you first need to have cookiecutter installed. If you don't have it already, you can install it with:

```bash

pip install cookiecutter

```

Once you have `cookiecutter` installed, you can create a new project from this template by running:

```bash

cookiecutter https://github.com/agusmdev/fastapi-ddd-template.git
```

This will prompt you for some information about your new project, such as the project name and the the main entity of your project. Then it will create a new project directory based on this template.


### Input variables

The generator (cookiecutter) will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values (some auto generated) are:

* `project_name`: The name of the project
* `project_slug`: The development friendly name of the project. By default, based on the project name
* `project_description`: Short description of your project
* `author`: Your name
* `first_entity`: Your project's first entity, start with a ready entity with CRUD operations


## 🍴 Setup after cloning the template

### Local 

To install the project locally, run the following scripts:


```bash
# Install the repository with its dependencies
$ ./scripts/install.sh
# Activate the environment
$ source scripts/venv.sh
```

## ⚙️ Usage

### Local

To run the service locally, execute the following script:


```shell
./scripts/run_app.sh
```

This command will start the service on port 8000.


## 🔧 Scripts

This is the list of commands implemented to facilitate the development of this project:

```text
clean.sh                 Remove temporary files
install.sh               Install the repository in the current directory
lint.sh                  Run linting on the source code
run_app.sh               Run the app
setup_dev.sh             Set up for local development
tests.sh                 Run a specific test suite
venv.sh                  Activate the environment created with virtualenv
```

## 🔍 Tests

To run the project tests, execute the following command:

```bash
# run unit tests
$ ./scripts/tests.sh unit

# run system tests
$ ./scripts/tests.sh system
```

By default, all unit tests defined in the project will be run.


## 🤝 Contributions

If you would like to contribute to the project, open a pull request or start a new issue!



