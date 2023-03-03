## FastAPI Template using the Repository Pattern Approach

This project is a backend template for a FastAPI-based application that uses the repository pattern approach to provide an abstraction layer between the business logic and the data access layer. It aims to provide a scalable and maintainable architecture for building web applications.


### Getting Started

To use this template, you first need to have cookiecutter installed. If you don't have it already, you can install it with:

```bash

pip install cookiecutter

```

Once you have `cookiecutter` installed, you can create a new project from this template by running:

cookiecutter https://github.com/agusmdev/fastapi-ddd-template.git

This will prompt you for some information about your new project, such as the project name and the the main entity of your project. Then it will create a new project directory based on this template.


### Input variables

The generator (cookiecutter) will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values (some auto generated) are:

* `project_name`: The name of the project
* `project_slug`: The development friendly name of the project. By default, based on the project name
* `first_entity`: Your project's first entity, it's just to get started with something


### ...