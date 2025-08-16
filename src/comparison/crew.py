# src/ai_tool_benchmark/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class ToolBenchmarkCrew():

    @agent
    def research_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['research_engineer'],
            verbose=True,
            tools=[SerperDevTool()]  # Use web search for live info
        )

    @agent
    def evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['evaluator'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )

    @task
    def evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluation_task'],
            output_file='output/tool_comparison_report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
