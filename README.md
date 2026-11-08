# Reinforcement Learning from Human Feedback for Safer Language Models

Reference implementation accompanying the paper *Reinforcement Learning from Human Feedback for Safer Language Models*.

Reward modeling and RLHF training scripts for safety preferences.

## Installation

```bash
git clone https://github.com/knobbyintens/rlhf-safety-emg2637.git
cd rlhf-safety-emg2637
pip install -r requirements.txt
```

## Repository layout

- `src/run_rlhf.py` — training / evaluation entry point
- `src/reward_model.py` — core implementation
- `tests/` — unit tests
