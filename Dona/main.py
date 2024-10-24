from crew import DirectoryAnalysisCrew

if __name__ == "__main__":
    directory_path = "./data"  # Change this to your target directory
    crew = DirectoryAnalysisCrew(directory_path)
    result = crew.run()
    print(result)
