from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from composio import Composio
from composio_crewai import CrewAIProvider

composio = Composio(provider=CrewAIProvider())
tools = composio.tools.get(
    user_id="pg-test-31059b7a-c708-4d4a-b8c5-4512e28dcb3c",
    toolkits=["GMAIL", "GOOGLECALENDAR"],
)


@CrewBase
class TelegramCrew:
    """TelegramCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def telegram_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["telegram_agent"], tools=tools, verbose=True
        )

    @task
    def telegram_task(self) -> Task:
        return Task(
            config=self.tasks_config["telegram_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TelegramCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
