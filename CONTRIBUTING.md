# 🤝 Contributing Guidelines

Contributions are always welcome!

To maintain a clean and readable history, we strictly follow a specific commit message convention. Please ensure your contributions adhere to the following structure.

## ✔️ Commit Guide

### The Structure

Every commit must consist of a **Header** and a **Body**, separated by an empty line.

```Plaintext
[TAG] (app_name) Capitalized short summary (50 chars or less)

[+] Detail about what was added
[-] Detail about what was removed
[*] Detail about what was changed/refactored
```

1. **The Header Rules**
    - **Imperative Mood:** Use "Add", "Fix", "Change" (not "Added", "Fixed", "Changed"). Think of the commit as an instruction.

    - **App Name:** mention the app name your commit is touching inside parenthesis.

    - **Allowed Tags:** Start your commit with one of the following:

      - `[INIT]`: Initializing a project or module.

      - `[ADD]`: Adding new features or files.

      - `[DEL]`: Removing files or features.

      - `[FIX]`: Fixing a bug.

      - `[REFACTOR]`: Changing code structure without changing behavior.

      - `[PERF]`: Improving performance.

      - `[STYLE]`: Formatting, missing semi-colons, etc. (no code change).

      - `[CHORE]`: Updating build tasks, package manager configs, etc.

2. **The Body Rules**

The body should list the specific changes made. Use the following bullets to categorize your changes:

- `[+]`: Used for creating files or adding significant code blocks.

- `[-]`: Used for deleting files or removing code.

- `[*]`: Used for modifying existing logic or file content.

### Example

#### ❌ Bad Commit

```Plaintext
added django files and fixed the readme
```

#### ✅ Good Commit

```Plaintext
[INIT] (core) Initialize Django Project structure

[+] Create Django core files (settings, urls, wsgi)
[+] Add docker-compose.yml for local development
[+] Add .gitignore to exclude pycache and env files
[*] Update README.md with setup instructions
```

## 🌿 Branching Strategy

We use a strict naming convention to keep track of features and fixes based on the application scope.

1. **Main Branches**
    - `main`: Production-ready code. Never push here.

    - `develop`: Integration branch. Target your Pull Requests here.

2. **Naming Your Branch**
Format: `type/app_name-description`

    |Type     |Use Case                         |Example                             |
    |---------|---------------------------------|------------------------------------|
    |`feat/`  |New features, Inits, Performance |`feat/payment-stripe-integration`   |
    |`fix/`   |Bug fixes, Refactoring, Style    |`fix/core-typo-in-readme`           |
    |`hotfix/`|Urgent production fixes          |`hotfix/disable-broken-endpoint`    |
    |`chore/` |Build, config, or auxiliary tools|`chore/docker-update-python-version`|

3. **Workflow**
    1. Checkout `develop` and pull the latest changes.

    2. Create your branch: `git checkout -b feat/my-app-cool-feature`.

    3. Commit your work using the [Commit Guidelines](#️-commit-guide).

    4. Push and create a Pull Request to `develop`.
