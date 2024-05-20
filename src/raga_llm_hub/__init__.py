from .llm_eval import RagaLLMEval
from .rag_builder import RAGBuilder as RagaRAGBuilder


import requests

__version__ = "1.0.0.11.alpha.1"


def check_latest_version(package_name):
    """
    Check the latest version of the package on PyPI and inform the user if an update is available.
    """
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=3)
        response.raise_for_status()
        latest_version = response.json()["info"]["version"]
        if __version__ != latest_version:
            print(
                f"Update available for {package_name} package. Your version: {__version__}. Latest version: {latest_version}."
            )
            print(
                f"Run 'pip install --upgrade raga_llm_hub=={latest_version}' to update to the latest version."
            )
    except Exception as e:
        print("Failed to check the latest package version:", e)


# Check the latest version
check_latest_version("raga_llm_hub")

__all__ = [
    "RagaLLMEval",
    "RagaRAGBuilder",
]
