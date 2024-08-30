# TaskTracker

**TaskTracker** is a simple command-line tool to manage tasks. It allows you to add, delete, update, and list tasks with various statuses such as "todo", "in progress", and "done". The application is built using Python and leverages the Fire library to create a command-line interface (CLI).

## Project Structure

```
.
├── db.json
├── taskTracker.py
└── utils
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   └── utils.cpython-312.pyc
    └── utils.py
```

- **db.json**: The JSON file used as the database to store tasks.
- **taskTracker.py**: The main script containing the CLI commands.
- **utils/**: Contains utility functions that handle the core functionality of the task manager.

## Features

- **Add Tasks**: Create new tasks with a title.
- **Delete Tasks**: Remove tasks by their ID.
- **Update Tasks**: Update the title of an existing task.
- **Mark Tasks**: Mark tasks as "in progress" or "done".
- **List Tasks**: View tasks filtered by status or view all tasks.

## Requirements

- Python 3.7+
- `fire` library (`pip install fire`)
- `tabulate` library (`pip install tabulate`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/TaskTracker.git
   cd TaskTracker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *If you haven't created a `requirements.txt` yet, you can create one with:*

   ```bash
   echo "fire\ntabulate" > requirements.txt
   ```

3. Run the CLI:

   ```bash
   python taskTracker.py <command> [arguments]
   ```

## Usage

Below are some examples of how to use the TaskTracker CLI:

### Add a Task

```bash
python taskTracker.py add "Finish the report"
```

### Delete a Task

```bash
python taskTracker.py delete 1
```

### Mark a Task as Done

```bash
python taskTracker.py mark_done 1
```

### List All Tasks

```bash
python taskTracker.py list all
```

### Update a Task

```bash
python taskTracker.py update 1 "Finalize the presentation"
```

## Contributing

Feel free to fork the repository and submit pull requests. For any major changes, please open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
