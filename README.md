## ISW221 | Familiar Tree

### Requirements

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (ultra-fast dependency manager)

### Installing Python and uv with Scoop (Windows)

1. **Install [Scoop](https://scoop.sh/):**

   Open PowerShell and run:
   ```sh
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

   ```

2. **Install Python and uv:**
   ```sh
   scoop install python
   scoop install uv
   ```

### Installation

1. **Clone the repository:**

   ```sh
   git clone git@github.com:ronz204/isw221-familiar-tree.git
   cd isw221-familiar-tree
   ```

2. **Install dependencies with uv:**

   ```sh
   uv pip install -r pyproject.toml
   ```

3. **(Optional but recommended) Activate the virtual environment:**

   On Windows:
   ```sh
   .venv\Scripts\activate
   ```

## Usage

To create the database tables and run the project, execute:

```sh
uv run src/Main.py
```

This will create the `tree.db` file and the necessary tables if they do not exist.

## Project Structure

- [`src/Main.py`](src/Main.py): Main script to initialize the database.
- [`src/Database/`](src/Database/): Database configuration and migrations.
- [`src/Models/`](src/Models/): Data models (Person, Family, Relationship).