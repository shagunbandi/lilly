from crewai import Agent
from tools.directory_reader import DirectoryReaderTool
from langchain.llms import Ollama


class Agents:
    def __init__(self):
        self.llm = Ollama(model="llama2")
        self.directory_reader_tool = DirectoryReaderTool()

    def directory_analyzer_agent(self):
        return Agent(
            role="Directory Analyzer",
            goal="Analyze directory contents and provide insights",
            backstory="""You are an expert in analyzing directory structures and files.
            Your expertise lies in understanding file organization and content patterns.""",
            tools=[self.directory_reader_tool],
            llm=self.llm,
            verbose=True,
        )

    def content_summarizer_agent(self):
        return Agent(
            role="Content Summarizer",
            goal="Summarize contents of files and provide key insights",
            backstory="""You are an expert in summarizing and extracting key information
            from various types of files. You excel at identifying patterns and important details.""",
            llm=self.llm,
            verbose=True,
        )
