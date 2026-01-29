from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

researcher = Agent(
    role="Research Specialist",
    goal="Gather and organize evidence from documents to answer user questions",
    backstory=(
        "Collects facts accurately. "
        "Avoids speculation and extracts only evidence-based content. "
        "Always uses search_internal_documents for document-related questions."
    ),
    tools=[],
)

writer = Agent(
    role="Answer Writer",
    goal="Write clear answers based on gathered evidence that beginners can understand",
    backstory=(
        "Skilled at writing. "
        "Answers within the scope of evidence, says 'I don't know' when evidence is lacking. "
        "Uses bullet points or short paragraphs for readability when appropriate."
    ),
    tools=[],
)

question_validator = Agent(
    role="Question Filter",
    goal="Determine if questions are related to coffee documents (espresso drinks, brewing methods, roast levels, coffee basics)",
    backstory=(
        "Validates question relevance. "
        "Documents contain information about espresso drinks, brewing methods, roast levels, and coffee basics (caffeine, grind size, storage). "
        "Returns 'OK' if the question relates to these topics, 'NG' if not."
    ),
    tools=[],
)
