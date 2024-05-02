from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI


@CrewBase
class InformationAnalystCrew():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.openai_llm = ChatOpenAI(
          temperature=0,
          model_name="gpt-4-turbo"
        )

    @agent
    def information_researcher(self) -> None:
        return Agent(
          config=self.agents_config['info_researcher'],
          llm=self.openai_llm,
        )

    @agent
    def information_analyst(self) -> None:
        return Agent(
          config=self.agents_config['info_analyst'],
          llm=self.openai_llm
        )

    @task
    def information_researcher_task(self) -> Task:
        return Task(
          config=self.tasks_config['research_info_task'],
          agent=self.information_researcher()
        )

    @task
    def information_analyst_task(self) -> Task:
        return Task(
          config=self.tasks_config['analyze_info_task'],
          agent=self.information_analyst()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
          agents=self.agents,
          tasks=self.tasks,
          process=Process.sequential,
          verbose=2,
        )
