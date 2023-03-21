# Contributing to {{cookiecutter.project_name| lower}}-backend

Thank you for your interest in contributing to {{cookiecutter.project_name| lower}}-backend! Below are guidelines and recommendations for contributing to this project. By following these guidelines, we ensure that the contribution process is easy and effective for everyone.

## Git Flow
This repository uses the [Git Flow](https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow) strategy. This means that there are two main branches in the repository: `main` and `develop`. The `main` branch contains code that is currently in production, while the `develop` branch contains code under development.

Each new feature or change must be developed in a separate feature branch from `develop`. When the work is completed, it is merged into `develop`. Then, after testing has been passed and everything has been verified to be working correctly, the `develop` branch is merged into the `main` branch.

## Guidelines for contributing
1. Create a fork of this repository on GitHub.
2. Clone your fork on your local computer.
3. Create a new branch from the `develop` branch with a descriptive name that indicates the change you are making. For example: `feature/new-functionality` or `bugfix/error-in-x-functionality`.
4. Make your changes to your branch.
5. Make sure that all tests pass and that the code is correctly formatted. There are certain pre-commit and pre-push checks in place that will validate this, and will not let commits through that do not meet these criteria.
6. Make commits with descriptive and consistent messages that clearly explain what you are doing in each commit. We suggest implementing the convention of [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) (e.g. "fix: fixed injection in MemoryRepo", "feat: new endpoint in {{cookiecutter.first_entity}}").
7. Publish your branch to your fork on GitHub.
8. Create a Pull Request from your branch to the develop branch of the original repository.
9. Wait for someone to review your Pull Request and make comments. If necessary, make changes to your branch and make more commits.
10. When your Pull Request is approved, it will be merged into the `develop` branch.
11. When it is deemed that there are enough features and bug fixes in `develop`, a new production version will be created by merging `develop` into `main`.

## Additional tips
- Keep your branches up to date with the `develop` branch of the original repository. To do this, first add the original repository as remote and then run `git pull` on the `develop` branch before creating a new feature branch. This way, you make sure that your new branch has the latest updates.
- If you have any questions, feel free to open an issue in the repository. If you need help with a particular Pull Request, you can tag a specific contributor to help you review it.

Thanks again for your interest in contributing to {{cookiecutter.project_name| lower}}-backend! If you have any questions or suggestions on how to improve these guidelines, feel free to let us know.