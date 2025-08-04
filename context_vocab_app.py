import argparse

class ContextVocabularyApp:
    """Prototype app that serves vocabulary based on a given context."""

    def __init__(self) -> None:
        # Static mapping of context names to vocabulary lists
        self.context_vocab = {
            "cafe": ["coffee", "tea", "cup"],
            "supermarket": ["milk", "bread", "checkout"],
            "train_station": ["ticket", "platform", "departure"],
        }

    def get_vocab_for(self, context: str) -> list[str]:
        """Return vocabulary words for the provided context name."""
        return self.context_vocab.get(context.lower(), [])


def main() -> None:
    parser = argparse.ArgumentParser(description="Context-based vocabulary app.")
    parser.add_argument(
        "--context",
        help="Name of the current context or location",
        required=True,
    )
    args = parser.parse_args()

    app = ContextVocabularyApp()
    vocab = app.get_vocab_for(args.context)

    if vocab:
        print(f"Vocabulary for {args.context}:")
        for word in vocab:
            print(f"- {word}")
    else:
        print(f"No vocabulary for context '{args.context}'.")


if __name__ == "__main__":
    main()
