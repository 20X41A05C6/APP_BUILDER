# API Documentation

This document provides detailed API documentation for all functions and classes.

## Functions

### main.py

#### main

---

### agent\graph.py

#### planner_agent

**Parameters:**

- `state`: dict

**Returns:** `dict`

---

#### architect_agent

**Parameters:**

- `state`: dict

**Returns:** `dict`

---

#### coder_agent

**Parameters:**

- `state`: dict

**Returns:** `dict`

---

### agent\prompts.py

#### planner_prompt

**Parameters:**

- `user_prompt`: str

**Returns:** `str`

---

#### architect_prompt

**Parameters:**

- `plan`: str

**Returns:** `str`

---

#### coder_system_prompt

**Returns:** `str`

---

### agent\tools.py

#### safe_path_for_project

**Parameters:**

- `path`: str

**Returns:** `pathlib.Path`

---

#### write_file

Writes content to a file at the specified path within the project root.

**Parameters:**

- `path`: str
- `content`: str

**Returns:** `str`

---

#### read_file

Reads content from a file at the specified path within the project root.

**Parameters:**

- `path`: str

**Returns:** `str`

---

#### get_current_directory

Returns the current working directory.

**Returns:** `str`

---

#### list_files

Lists all files in the specified directory within the project root.

**Parameters:**

- `directory`: str

**Returns:** `str`

---

#### run_cmd

Runs a shell command in the specified directory and returns the result.

**Parameters:**

- `cmd`: str
- `cwd`: str
- `timeout`: int

**Returns:** `Tuple[int, str, str]`

---

#### init_project_root

---

## Classes

### agent\states.py

#### File

**Inherits from:** BaseModel

---

#### Plan

**Inherits from:** BaseModel

---

#### ImplementationTask

**Inherits from:** BaseModel

---

#### TaskPlan

**Inherits from:** BaseModel

---

#### CoderState

**Inherits from:** BaseModel

---
