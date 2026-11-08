"""Entry point for Reinforcement Learning from Human Feedback for Safer Language Models."""

from .reward_model import build_model


def main():
    model = build_model()
    print("ready:", model)


if __name__ == "__main__":
    main()
