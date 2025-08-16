# src/ai_tool_benchmark/main.py
from comparison.crew import ToolBenchmarkCrew

from datetime import datetime

def run():
    inputs = {
        "current_date": str(datetime.now())
    }

    result = ToolBenchmarkCrew().crew().kickoff(inputs=inputs)
    print("\n\n=== FINAL BENCHMARK REPORT ===\n\n")
    print(result.raw)

if __name__ == "__main__":
    run()
