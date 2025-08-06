import argparse
import json
import os

DATA_FILE = "notes.json"


def load_notes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_notes(notes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)


def add(args):
    notes = load_notes()
    next_id = notes[-1]["id"] + 1 if notes else 1
    note = {
        "id": next_id,
        "text": args.text,
        "due": args.due,
        "done": False,
    }
    notes.append(note)
    save_notes(notes)
    print(f"Added note {next_id}")


def list_notes(_args):
    notes = load_notes()
    for n in notes:
        status = "\u2713" if n["done"] else "\u2717"
        due = f" (due {n['due']})" if n["due"] else ""
        print(f"{n['id']}. [{status}] {n['text']}{due}")


def mark_done(args):
    notes = load_notes()
    for n in notes:
        if n["id"] == args.id:
            n["done"] = True
            save_notes(notes)
            print(f"Note {args.id} marked as done")
            break
    else:
        print("Note not found")


def main():
    parser = argparse.ArgumentParser(description="Simple note and task planner")
    subparsers = parser.add_subparsers(dest="command")

    p_add = subparsers.add_parser("add", help="Add a note or task")
    p_add.add_argument("text", help="Text of the note or task")
    p_add.add_argument("--due", help="Optional due date (YYYY-MM-DD)")
    p_add.set_defaults(func=add)

    p_list = subparsers.add_parser("list", help="List notes and tasks")
    p_list.set_defaults(func=list_notes)

    p_done = subparsers.add_parser("done", help="Mark a note or task as done")
    p_done.add_argument("id", type=int, help="ID of the note/task")
    p_done.set_defaults(func=mark_done)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
