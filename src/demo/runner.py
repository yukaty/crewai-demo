from crewai import Crew, Process
from demo.agents import question_validator, researcher, writer
from demo.tasks import search_task, validation_task, write_task


def run_crew(question: str) -> str:
    crew = Crew(
        agents=[question_validator, researcher, writer],
        tasks=[validation_task, search_task, write_task],
        process=Process.sequential,  # agents and tasks are executed in order
        verbose=False,
    )

    result = crew.kickoff(inputs={"question": question})
    return str(result)
