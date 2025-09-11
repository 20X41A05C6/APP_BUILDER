# Project Documentation

This documentation is automatically generated and maintained by the Auto Documentation Agent.

## Project Overview

This project contains the following components:

### Python Files

- **main.py**

- **agent\graph.py**

- **agent\prompts.py**

- **agent\states.py**

- **agent\tools.py**

## API Documentation

### Functions

#### main.py

**main**

#### agent\graph.py

**planner_agent**
  - Parameters: state
  - Returns: dict

**architect_agent**
  - Parameters: state
  - Returns: dict

**coder_agent**
  - Parameters: state
  - Returns: dict

#### agent\prompts.py

**planner_prompt**
  - Parameters: user_prompt
  - Returns: str

**architect_prompt**
  - Parameters: plan
  - Returns: str

**coder_system_prompt**
  - Returns: str

#### agent\tools.py

**safe_path_for_project**
  - Parameters: path
  - Returns: pathlib.Path

**write_file**
  - Writes content to a file at the specified path within the project root.
  - Parameters: path, content
  - Returns: str

**read_file**
  - Reads content from a file at the specified path within the project root.
  - Parameters: path
  - Returns: str

**get_current_directory**
  - Returns the current working directory.
  - Returns: str

**list_files**
  - Lists all files in the specified directory within the project root.
  - Parameters: directory
  - Returns: str

**run_cmd**
  - Runs a shell command in the specified directory and returns the result.
  - Parameters: cmd, cwd, timeout
  - Returns: Tuple[int, str, str]

**init_project_root**

### Classes

#### agent\states.py

**File**
  - Inherits from: BaseModel

**Plan**
  - Inherits from: BaseModel

**ImplementationTask**
  - Inherits from: BaseModel

**TaskPlan**
  - Inherits from: BaseModel

**CoderState**
  - Inherits from: BaseModel
