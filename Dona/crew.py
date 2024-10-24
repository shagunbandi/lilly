from crewai import Crew
from agents import Agents
from tasks import Tasks


class DirectoryAnalysisCrew:
    def __init__(self, directory_path: str):
        self.agents = Agents()
        self.tasks = Tasks()
        self.directory_path = directory_path

    def run(self):
        # Initialize agents
        analyzer = self.agents.directory_analyzer_agent()
        summarizer = self.agents.content_summarizer_agent()

        # Create tasks
        analysis_task = self.tasks.analyze_directory(analyzer, self.directory_path)

        summary_task = self.tasks.summarize_contents(
            summarizer,
            analysis_task.output,  # This will be the output from the first task
        )

        # Create crew
        crew = Crew(
            agents=[analyzer, summarizer],
            tasks=[analysis_task, summary_task],
            verbose=True,
        )

        # Start the crew
        result = crew.kickoff()
        return result
