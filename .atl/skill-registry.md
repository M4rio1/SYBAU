# Skill Registry

## Loaded Skills

### ui-ux-pro-max
- **Trigger**: "plan, build, create, design, implement, review, fix, improve, optimize, enhance, refactor, and check UI/UX code" for "website, landing page, dashboard, admin panel, e-commerce, SaaS, portfolio, blog, and mobile app".
- **Compact Rules**:
> [!NOTE]
> **Core Principles for SYBAU**:
> - **Accessibility first**: Contrast 4.5:1, Aria-labels, Focus-states.
> - **Motion**: Duration 150–300ms, use spring-physics for a natural feel (Motion/Framer Motion).
> - **Tailwind**: Use semantic color tokens, avoid raw hex.
> - **Layout**: Mobile-first, respect Safe Areas (for notched devices).
> - **Anti-patterns**: No emojis as structural icons, avoid layout-shifting animations.

### database-schema-designer
- **Trigger**: "design robust, scalable database schemas", "normalization guidelines", "indexing strategies", "migration patterns".
- **Compact Rules**:
> [!NOTE]
> - **Normalization**: 3NF for OLTP, Denormalization for OLAP.
> - **Performance**: Composite indexes for multi-field queries, avoid SELECT * in high-load apps.
> - **Constraints**: Use foreign keys and CHECK constraints to ensure data integrity at the DB level.

### branch-pr
- **Trigger**: "creating a pull request", "opening a PR", "preparing changes for review".
- **Compact Rules**:
> [!NOTE]
> - **Issue First**: Ensure an issue exists and is linked in the PR.
> - **Context**: Provide clear summary and testing evidence.
> - **Commits**: Use conventional commits (feat, fix, refactor).

### issue-creation
- **Trigger**: "creating a GitHub issue", "reporting a bug", "requesting a feature".
- **Compact Rules**:
> [!NOTE]
> - **Clarity**: Precise title and descriptive body.
> - **Acceptance Criteria**: Define exactly when the issue is closed.

### judgment-day
- **Trigger**: "judgment day", "review adversarial", "dual review", "juzgar".
- **Compact Rules**:
> [!NOTE]
> - **Adversarial**: Force agents to find flaws that standard reviews miss.
> - **Iterative**: Re-judge until both judges pass.

## Project Standards (auto-resolved)

- **Monorepo Structure**: Keep `frontend/` and `backend/` decoupled. Communicate via REST/SSE.
- **Frontend**: React 19 + TypeScript + Tailwind 4. Use Vite for development.
- **Backend**: Flask + Whisper + Ollama Proxy. Keep it thin and stateless where possible.
- **Testing**: CURRENTLY DISABLED. Manual verification required for all changes until Vitest/Pytest are added.
