from crewai import Task

from demo.agents import question_validator, researcher, writer
from demo.tools import search_internal_documents

validation_task = Task(
    description=(
        "User's question is: '{question}'.\n"
        "Determine if this question is related to coffee documents (espresso drinks, brewing methods, roast levels, caffeine, grind size, storage).\n"
        "If related, output 'OK' only.\n"
        "If not related, output 'NG: This question is outside the scope of our coffee documents. We can only answer questions about espresso drinks, brewing methods, roast levels, and coffee basics.'\n"
    ),
    expected_output="'OK' or 'NG: reason'",
    agent=question_validator,
)

search_task = Task(
    description=(
        "User's question is: '{question}'.\n"
        "Only if the previous task returned 'OK', use the search_internal_documents tool to gather evidence.\n"
        "If the result was 'NG', skip the search and output 'Search skipped - question is out of scope'.\n"
        "Format your output as follows:\n"
        "1) Evidence (citations): Extract and list important passages from search results\n"
        "2) Key points: Bullet points of information to use in the answer\n"
        "Note: No speculation allowed. If there's no evidence, write 'No evidence found'.\n"
    ),
    expected_output="Evidence (citations) and key points in bullet format, or out-of-scope message",
    agent=researcher,
    tools=[search_internal_documents],
    context=[validation_task],
)

write_task = Task(
    description=(
        "User's question is: '{question}'.\n"
        "Check the question filter's validation result.\n"
        "If the result was 'NG', respond with: 'I apologize, but this question is outside the scope of our coffee documents. We can only answer questions about espresso drinks, brewing methods, roast levels, and coffee basics.'\n"
        "If the result was 'OK', write a final answer for the user based on the evidence and key points gathered by the previous task.\n"
        "Rules:\n"
        "- Answer within the scope of evidence (if no evidence, clearly state that it's unknown)\n"
        "- Clearly state important conditions or numbers\n"
        "- End with 'Referenced sources (excerpt)' with brief citations\n"
    ),
    expected_output="Final answer based on evidence for the user, or out-of-scope message",
    agent=writer,
    context=[validation_task, search_task],
)
