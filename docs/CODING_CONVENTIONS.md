# GreenRoute AKL Coding Conventions

## Python (Backend)

### General
- **Formatting:** Use [Black](https://black.readthedocs.io/en/stable/) for automatic code formatting.
- **Style Guide:** Follow [PEP8](https://peps.python.org/pep-0008/).
- **Type Hints:** Use type hints for all function signatures and variables (mypy compatible).
- **Imports:**
  - Group as: standard library → third-party → local imports, with a blank line between groups.
- **Naming:**
  - Variables & functions: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`
- **Line Length:** Max 88 characters.

### Documentation & Comments
- **Docstrings:**
  - All public classes and functions must include [Google-style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
- **Comments:**
  - Use comments to explain complex logic, not obvious code.

### Error Handling
- **Exceptions:**
  - Catch specific exceptions, not `Exception`.
  - Sanitize errors before exposing to clients (never leak stack traces).
- **Logging:**
  - Use Python’s `logging` module for error and info logs.

### Security & Best Practices
- No global variables for shared state.
- Validate all input/output schemas with Pydantic.
- Never store plaintext passwords.
- No blocking code in `async def` endpoints.

---

## React (Frontend)

### General
- **Formatting:** Use [Prettier](https://prettier.io/) and [ESLint](https://eslint.org/) (Airbnb/Next.js rules).
- **Functional Components:** Only use functional components and hooks.
- **Naming:**
  - Components & Classes: `PascalCase`
  - Variables & Functions: `camelCase`
  - File names: `camelCase` or `kebab-case` (e.g., `routePlanner.js`, `route-planner.jsx`)
  - Hooks start with `use` (e.g., `useAuth`)
- **File Size:**
  - Keep components under 100 lines if possible.
  - One component per file.

### Documentation & Comments
- **Comments:**
  - Explain non-obvious logic, especially for hooks and context.
- **Prop Types:**
  - All props and state should be typed using `interface` or `type` (if using TypeScript).

### Layout & Styling
- **No inline styles for layout:**
  - Use CSS modules, styled-components, or Tailwind.
- **No deeply nested components:**
  - Avoid “div soup.”

### State & Data
- **State:**
  - Use context for shared state, not prop drilling.
  - Never mutate state directly.
- **Data Fetching:**
  - API/data fetching only in service files or hooks, not inside component bodies.
  - Use `useEffect` for side effects, never fetch in render.

### Error Handling
- **Error Boundaries:**
  - Use error boundaries for catching UI exceptions.

---

## Committing to These Conventions

- Add this file as `CODING_CONVENTIONS.md` to your repo.
- Reference it in your `README.md` (e.g., “See `CODING_CONVENTIONS.md` for our full coding standards.”)
- Use tools like Prettier, Black, ESLint, and mypy to **enforce** these rules before merging PRs.
- All team members (including yourself) should review new code for adherence to these conventions during code review.
