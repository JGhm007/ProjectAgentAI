# main.py
from tasks import get_sample_tasks
from agent import PlanningAgent

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

if __name__ == "__main__":
    run_app()