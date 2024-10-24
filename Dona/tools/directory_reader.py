from langchain.tools import BaseTool
import os
from typing import List

class DirectoryReaderTool(BaseTool):
    name = "Directory Reader"
    description = "Reads and analyzes contents of a directory"

    def _run(self, path: str) -> List[str]:
        """Read contents of a directory."""
        try:
            contents = []
            for root, dirs, files in os.walk(path):
                for name in files:
                    file_path = os.path.join(root, name)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            contents.append({
                                'path': file_path,
                                'content': content
                            })
                    except Exception as e:
                        contents.append({
                            'path': file_path,
                            'error': str(e)
                        })
            return contents
        except Exception as e:
            return f"Error reading directory: {str(e)}"

    async def _arun(self, path: str) -> List[str]:
        """Async implementation of run."""
        return self._run(path)
