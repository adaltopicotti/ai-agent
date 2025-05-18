from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    formatted_text = f"--- Research Output --- {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text)

    return f"Data successfully saved to {filename}"


save_tool = Tool(
    name="save_text_to_file",
    description="Save structured research data to a text file.",
    func=save_to_txt
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    description="Search the web for information",
    func=search.run
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = Tool(
    name="wikipedia",
    description="Search Wikipedia for information",
    func=api_wrapper.run
)
