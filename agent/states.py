from pydantic import BaseModel, Field,ConfigDict

class File(BaseModel):
    path: str = Field(description="The path to the file to be created or modified")
    purpose: str = Field(description="The purpose of the file, e.g. 'main application logic', 'data processing module', etc.")
    
class Plan(BaseModel):
    name: str=Field( description="name of the project")
    description: str=Field( description="A online description of the app to be built ,e.g 'A web application managing tasks'")
    techstack: str=Field( description="The technology stack to be used for app,e.g 'python,java script,React,flask'")
    features: list[str]=Field( description="A list of features to be implemented in the app e.g. 'user authentication','task creation','task deletion'")
    files: list[File]=Field( description="A list of files to be created in the project e.g. 'app.py','requirements.txt','templates/index.html'")


class ImplementationTask(BaseModel):
    filepath: str=Field( description="path of the file to be created or modified in the project e.g. 'app.py','requirements.txt','templates/index.html'")
    taskdescription: str=Field( description="A detailed description of the implementation task, including what to implement, variable and function names, dependencies, and integration details.")

class TaskPlan(BaseModel):
    Implementation_steps: list[ImplementationTask]=Field( description="A list of implementation tasks to be performed in the project")
    model_config = ConfigDict(extra="allow")

class CoderState(BaseModel):
    task_plan: TaskPlan=Field( description="The complete task plan with all implementation steps")
    current_step_idx: int=Field(0, description="The index of the current implementation step being worked on")
    current_file_content: str=Field(None, description="The existing content of the file being worked on, if any")
