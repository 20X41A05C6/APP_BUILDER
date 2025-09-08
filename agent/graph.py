from dotenv import load_dotenv
load_dotenv()
import os


from langchain.globals import set_debug, set_verbose
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph ,END
from langgraph.prebuilt import create_react_agent  
from prompts import *
from states import *
from tools import write_file, read_file, get_current_directory, list_files


set_debug(True)
set_verbose(True)

llm=ChatGroq(model="qwen/qwen3-32b")

#prompt=planner_prompt(user_prompt="Build a task management app")
#user_prompt="Build a task management app"

def planner_agent(state: dict) -> dict:
    user_prompt=state['user_prompt']
    response=llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
    if response is None:
        raise ValueError("No response from planner agent")
    return {"plan": response}


def architect_agent(state: dict) -> dict:
    plan:Plan=state['plan']
    response=llm.with_structured_output(TaskPlan).invoke(architect_prompt(plan=plan.model_dump_json()))
    if response is None:
        raise ValueError("No response from architect agent")
    response.plan=plan
    return {"task_plan": response}

def coder_agent(state: dict) -> dict:
    coder_state=state.get("coder_state")
    if coder_state is None:
        coder_state=CoderState(task_plan=state['task_plan'], current_step_idx=0)

    steps=coder_state.task_plan.Implementation_steps
    if coder_state.current_step_idx >= len(steps):
        return {"status": "DONE", "coder_state": coder_state}    


    current_task=steps[coder_state.current_step_idx]
    existing_content=read_file.run(current_task.filepath)
    
    system_prompt=coder_system_prompt()
    user_prompt=(
        f"Task: {current_task.taskdescription}\n"
        f"File: {current_task.filepath}\n"
        f"Existing content:\n{existing_content}\n"
        "use write_file(path,content) to save the changes."
    )

    
    #response=llm.invoke(system_prompt+user_prompt)
    coder_tools = [read_file, write_file, list_files, get_current_directory]
    react_agent = create_react_agent(llm, coder_tools)

    react_agent.invoke({"messages": [{"role": "system", "content": system_prompt},
                                     {"role": "user", "content": user_prompt}]})

    coder_state.current_step_idx += 1
    return {"coder_state": coder_state}
       
graph=StateGraph(dict)

graph.add_node("planner",planner_agent)
graph.add_node("architect",architect_agent)
graph.add_node("coder",coder_agent)


graph.add_edge("planner", "architect")
graph.add_edge("architect", "coder")
graph.add_conditional_edges(
    "coder",
    lambda s: "END" if s.get("status") == "DONE" else "coder",
    {"END": END, "coder": "coder"}
)
# graph.add_conditional_edges(
#     "coder",
#     lambda s:"END" if s.get("status")=="DONE" else "coder",
#     {"END":  END, "coder": "coder"}
# )


graph.set_entry_point("planner")

agent=graph.compile()

if __name__=="__main__":

    user_prompt="Build a task managment app in html css js . connect html css jss and give me best code"
    result=agent.invoke({"user_prompt": user_prompt}, 
                          {"recursion_limit": 100})
    print(result)

