# main.py
from tasks import get_sample_tasks
from agent import PlanningAgent

#Update 3
def save_to_file(content):
    with open("plan_content.txt", "w") as file:
        file.write(content)
    print("Plan saved to plan_content.txt")


def run_app():
    print("Starting Planning System...")
    
    # 1. Get tasks
    my_tasks = get_sample_tasks()
    
    # 2. Initialize Agent
    bot = PlanningAgent()
    
    # 3. Run action
    plan = bot.plan_tasks(my_tasks)
    
    print("\n--- AGENT RESULT ---")
    print(plan)
    
    # 4. Save to file
    save_to_file(plan)  

if __name__ == "__main__":
    run_app()