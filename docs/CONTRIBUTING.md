# Contributing to The Polyglot Codebase

Thank you for your interest in contributing to the **50 Languages Polyglot Codebase**!

## How Can You Contribute?
1. **Report bugs or outdated commands**: Submit an issue if a compiler flag or package manager command is deprecated.
2. **Improve comments or documentation**: Make explanations clearer and more educational.
3. **Add future roadmap implementations**: Help implement Stage 2 (Variables & Types) or Stage 3 (Algorithms).

## Guidelines for Adding or Modifying a Language
Every language directory under `languages/` must adhere to this structure:
- Follow standard idiomatic naming convention (e.g., `01-python`, `04-c`).
- Provide clean, idiomatic source code with clear inline explanations.
- Include a dedicated `README.md` detailing:
  - Language metadata (paradigm, year, creator).
  - Prerequisites and installation command.
  - Step-by-step terminal run commands.
  - Expected stdout output.

## Code Style
- Use idiomatic code formatting standard to that language (PEP8 for Python, `gofmt` for Go, `rustfmt` for Rust, etc.).
- Avoid obfuscated code; favor clarity and educational value over code golf.
