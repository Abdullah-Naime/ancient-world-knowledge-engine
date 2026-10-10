\# Ancient World Knowledge Engine



A Python and Prolog-driven CLI application that uses logical rule-based inference and a historical knowledge base to solve archaeological mysteries.



\## Overview

The \*\*Ancient World Knowledge Engine\*\* combines Python's user interaction capabilities with SWI-Prolog's declarative logic programming engine. The system queries structured historical facts (geographical regions, river systems, writing scripts, rulers, and artifacts) and applies logical inference rules to identify matching civilizations or solve multi-clue archaeological dig scenarios.



\## Features

\- \*\*Logical Search Engine:\*\* Query ancient civilizations by writing systems, river basins, or geographic regions.

\- \*\*Archaeological Dig Solver:\*\* Supply recovered artifacts and clues (e.g., river location + writing script) to let Prolog dynamically infer matching civilizations.

\- \*\*Dossier Retrieval:\*\* Fetch linked rulers, artifacts, and geographical profiles via rule unification.

\- \*\*Hybrid System Architecture:\*\* Python handles CLI execution and process control while SWI-Prolog executes backend deduction.



\## Architecture \& Project Structure

\- `kb.pl` — Knowledge base containing atomic historical facts.

\- `rules.pl` — Prolog inference rules and logical predicates.

\- `main.py` — Python CLI wrapper managing subprocess communication with SWI-Prolog.



\## Requirements

\- \*\*Python 3.x\*\*

\- \*\*SWI-Prolog\*\* (`swipl` installed and added to system PATH)



\## Getting Started



1\. Clone the repository:

&#x20;  ```bash

&#x20;  git clone \[https://github.com/Abdullah-Naime/ancient-world-knowledge-engine.git](https://github.com/Abdullah-Naime/ancient-world-knowledge-engine.git)

&#x20;  cd ancient-world-knowledge-engine

