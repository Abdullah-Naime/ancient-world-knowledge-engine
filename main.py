# main.py - Python CLI wrapper for Prolog Engine
import subprocess
import re
import sys


def query_prolog(goal_query):
    """Executes a query against rules.pl using SWI-Prolog subprocess."""
    cmd = [
        "swipl", "-g",
        f"consult('rules.pl'), forall({goal_query}, (write('MATCH:'), writeln({goal_query}))), halt."
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    matches = []
    for line in result.stdout.splitlines():
        if line.startswith("MATCH:"):
            matches.append(line.replace("MATCH:", "").strip())
    return matches


def solve_mystery():
    print("\n" + "=" * 50)
    print("  🕵  ARCHAEOLOGICAL DIG MYSTERY SOLVER")
    print("=" * 50)
    river = input("Enter recovered river artifact clue (e.g. euphrates, nile, indus): ").strip().lower()
    writing = input("Enter writing script clue (e.g. cuneiform, hieroglyphs): ").strip().lower()

    query = f"identify_dig_site({river}, {writing}, Civ)"
    results = query_prolog(query)

    print("\n Analyzing logical evidence with Prolog...")
    if results:
        print("\n Match Found!")
        for res in set(results):
            # Extract civilization name from Prolog output predicate format
            match_civ = re.search(r'identify_dig_site\(.*,.*,\s*([a-z_]+)\)', res)
            civ_name = match_civ.group(1) if match_civ else res
            print(f" -> Likely Civilization: {civ_name.upper().replace('_', ' ')}")
    else:
        print("\n❌ No historical matches found for this clue combination.")


def search_by_writing():
    print("\n" + "=" * 50)
    print("   SEARCH BY WRITING SYSTEM")
    print("=" * 50)
    system = input("Enter writing system (e.g. cuneiform, hieroglyphs): ").strip().lower()

    query = f"civilization_by_writing({system}, Civ)"
    results = query_prolog(query)

    if results:
        print(f"\nMatching civilizations for '{system}':")
        seen = set()
        for res in results:
            match_civ = re.search(r'civilization_by_writing\(.*,\s*([a-z_]+)\)', res)
            civ_name = match_civ.group(1) if match_civ else res
            if civ_name not in seen:
                seen.add(civ_name)
                print(f" • {civ_name.replace('_', ' ').title()}")
    else:
        print(f"\nNo civilizations found for '{system}'.")


def main_menu():
    while True:
        print("\n" + "🏛️ " * 5 + " ANCIENT WORLD KNOWLEDGE ENGINE " + "🏛️ " * 5)
        print("1. Search Civilizations by Writing System")
        print("2. Solve Archaeological Dig Mystery (River + Writing Clues)")
        print("3. Exit Engine")

        choice = input("\nSelect an option (1-3): ").strip()

        if choice == "1":
            search_by_writing()
        elif choice == "2":
            solve_mystery()
        elif choice == "3":
            print("\nShutting down engine. Farewell!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()