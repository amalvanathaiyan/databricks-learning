"""Rebuild interview_prep/question_bank.md from the Interview Q&A callouts in every notebook.

Usage (from the repo root):
    python tools/build_question_bank.py
"""
import html
import json
import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parent.parent
FOLDER_TITLES = {
    "00_platform_tour": "00 Platform tour",
    "01_spark_basics": "01 Spark basics",
    "02_spark_internals": "02 Spark internals",
    "03_delta_lake": "03 Delta Lake",
    "04_databricks": "04 Databricks",
    "05_optimization": "05 Optimization",
    "06_unity_catalog": "06 Unity Catalog",
    "07_workflows": "07 Workflows",
    "08_streaming_and_ingestion": "08 Streaming and ingestion",
    "09_azure_databricks": "09 Azure Databricks",
}
# One question: <b>🎤 N. question</b><br> answer ... up to the next question or the end of the callout
QUESTION = re.compile(r"<b>🎤 \d+\. (.*?)</b><br>\s*(.*?)(?=<br><br>|\n</div>)", re.S)


def to_markdown(text):
    """Turn the small amount of HTML used in callouts back into markdown."""
    text = re.sub(r"<code>(.*?)</code>", lambda m: "`" + html.unescape(m.group(1)) + "`", text)
    text = re.sub(r"</?b>", "**", text)
    text = re.sub(r"<br\s*/?>", " ", text)
    return html.unescape(re.sub(r"<[^>]+>", "", text)).strip()


def questions_in(notebook_path):
    nb = json.loads(notebook_path.read_text(encoding="utf-8"))
    found = []
    for cell in nb["cells"]:
        source = "".join(cell["source"])
        if cell["cell_type"] == "markdown" and "🎤" in source:
            found += [(to_markdown(q), to_markdown(a)) for q, a in QUESTION.findall(source)]
    return found


def main():
    sections, total, lesson_count = [], 0, 0
    for folder, title in FOLDER_TITLES.items():
        notebooks = sorted((REPO / folder).glob("*.ipynb"))
        lessons = [(nb.stem, questions_in(nb)) for nb in notebooks]
        lessons = [(name, qs) for name, qs in lessons if qs]
        if not lessons:
            continue
        sections += [f"## {title}", ""]
        for name, qs in lessons:
            sections += [f"### {name}", ""]
            for i, (q, a) in enumerate(qs, 1):
                sections += [f"**{i}. {q}**", "", a, ""]
            total += len(qs)
            lesson_count += 1

    header = [
        "# Question Bank",
        "",
        "Interview questions from every lesson, with short spoken-style answers.",
        "Practise by covering the answer, saying yours out loud, then comparing.",
        "",
        f"**{total} questions** across {lesson_count} lessons.",
        "",
        "Generated from each notebook's **Interview Q&A** section by `tools/build_question_bank.py`.",
        "Edit the notebooks, then run the script again.",
        "",
    ]
    out = REPO / "interview_prep" / "question_bank.md"
    out.write_text("\n".join(header + sections), encoding="utf-8")
    print(f"{total} questions from {lesson_count} lessons -> {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
