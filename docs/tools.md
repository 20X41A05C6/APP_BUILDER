# agent\tools.py

## Functions

### safe_path_for_project

**Parameters:**

- `path`: str

**Returns:** `pathlib.Path`

### write_file

Writes content to a file at the specified path within the project root.

**Parameters:**

- `path`: str
- `content`: str

**Returns:** `str`

### read_file

Reads content from a file at the specified path within the project root.

**Parameters:**

- `path`: str

**Returns:** `str`

### get_current_directory

Returns the current working directory.

**Returns:** `str`

### list_files

Lists all files in the specified directory within the project root.

**Parameters:**

- `directory`: str

**Returns:** `str`

### run_cmd

Runs a shell command in the specified directory and returns the result.

**Parameters:**

- `cmd`: str
- `cwd`: str
- `timeout`: int

**Returns:** `Tuple[int, str, str]`

### init_project_root
