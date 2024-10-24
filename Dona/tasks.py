from crewai import Task
from typing import List


class Tasks:
    def analyze_directory(self, agent, directory_path: str) -> Task:
        return Task(
            description=f"""
            1. Analyze the directory at {directory_path}
            2. List all files and their types
            3. Identify patterns in file organization
            4. Report any potential issues or anomalies
            """,
            agent=agent,
        )

    def summarize_contents(self, agent, files: List[dict]) -> Task:
        return Task(
            description=f"""
            1. Review the contents of all readable files
            2. Provide a summary of key findings
            3. Identify common themes or patterns
            4. Highlight any important information discovered
            """,
            agent=agent,
        )
