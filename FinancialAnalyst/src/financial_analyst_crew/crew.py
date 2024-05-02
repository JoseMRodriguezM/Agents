from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
# from langchain.llms import Ollama


@CrewBase
class FinancialAnalystCrew():
    """Financial Analyst crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        super().__init__()
        self.groq_llm = ChatGroq(
         temperature=0,
         model_name="llama3-70b-8192"
        )
        # self.ollama_llm = Ollama(model='llama3')

    @agent
    def company_researcher(self) -> None:
        return Agent(
          config=self.agents_config['company_researcher'],
          llm=self.groq_llm
        )

    @agent
    def company_analyst(self) -> None:
        return Agent(
          config=self.agents_config['company_analyst'],
          llm=self.groq_llm
        )

    @agent
    def plotter(self) -> None:
        return Agent(
          config=self.agents_config['plotter'],
          llm=self.groq_llm
        )

    @task
    def reseacher_company_task(self) -> Task:
        return Task(
          config=self.tasks_config['research_company_task'],
          agent=self.company_researcher()
        )

    @task
    def analyze_company_task(self) -> Task:
        return Task(
          config=self.tasks_config['analyze_company_task'],
          agent=self.company_analyst()
        )

    @task
    def plotter_company_task(self) -> Task:
        return Task(
          config=self.tasks_config['plotter_company_task'],
          agent=self.plotter(),
        )

    @crew
    def crew(self) -> Crew:
        """Create the FinancialAnalystCrew crew"""
        return Crew(
          agents=self.agents,
          tasks=self.tasks,
          process=Process.sequential,
          verbose=2,
        )
