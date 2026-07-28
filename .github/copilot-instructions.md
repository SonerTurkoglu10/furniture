<!--
Guidance for AI coding agents (Copilot / Codegen bots) working in this repository.

This repo currently appears empty. The instructions below are intentionally concise
and focused on discovery and safe, incremental edits. When the repository contains
source, follow the "Analysis checklist" to gather the project-specific facts and
then produce small, well-tested changes.
-->

# Copilot instructions — repository onboarding

- Purpose: Help an AI agent become productive quickly by describing discovery
  probes, merge behavior, and what to surface to the human if something is
  missing or ambiguous.

## Quick start (first actions)
1. Check if the repository is empty. If empty, ask the user where the project
   source lives or whether you should initialize files here.
2. If not empty, locate key manifest files (search for these at repo root):
   - `package.json`, `pnpm-lock.yaml`, `yarn.lock` (JavaScript/TypeScript)
   - `requirements.txt`, `pyproject.toml`, `Pipfile` (Python)
   - `go.mod` (Go), `pom.xml` (Java), `Cargo.toml` (Rust)
   - `Dockerfile`, `Makefile`, `README.md`
3. Locate any existing agent guidance files and merge rather than overwrite:
   - `.github/copilot-instructions.md`, `AGENT.md`, `AGENTS.md`, `CLAUDE.md`
   - `.cursor/rules/**`, `.windsurf/rules/**`, `.clinerules/**`, `.cursorrules`

## Analysis checklist (what to extract and document for humans/agents)
- Project type and primary language (manifest + typical source dirs `src/`,
  `app/`, `backend/`, `frontend/`).
- How to build locally: exact commands to install dependencies and run the
  project (examples: `npm install; npm run build`, `python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt`).
- How to run tests: exact commands, test folder names, and any environment
  variables required. If tests require services (DB, Redis), note docker-compose
  or local start commands.
- Linting and formatting: which tools and commands (ESLint, black, Prettier).
- Common runtime entrypoints (e.g., `app/main.py`, `src/index.ts`, `cmd/`),
  and where configuration lives (`.env`, `config/*.yaml`).
- Integration points: external APIs, databases, message brokers, auth providers.

## Writing or merging `.github/copilot-instructions.md`
- If this file already exists, preserve any human-written sections and only add
  project-specific facts you discovered. Keep changes small and explain reasons
  in the PR description.
- Prefer bullet lists with exact commands and key file locations (not vague
  prose). Example: "Run tests: PowerShell — `python -m pytest tests/ -q`".

## When the repo is empty (this repo right now)
- Do not scaffold large projects without explicit user permission.
- Ask the user one clear question: "Should I initialize a project here, or is
  the source located elsewhere? If elsewhere, please provide the path or a
  sample file to start from."

## Fail-fast signals to surface to humans
- Missing manifest files or build commands after scanning the repo root.
- Multiple conflicting build manifests (e.g., both `package.json` and
  `setup.py`) — ask which is primary.
- Tests failing after a small, well-scoped change — include failing test
  output and the minimal diff that caused it.

## Useful examples to include in edits (when present)
- Point to the canonical start file: `src/index.ts` or `app/main.py`.
- Reference database migration folder (e.g., `migrations/` or `alembic/`).
- Show how environment variables are loaded (e.g., `.env.example` -> `.env`).

## Interaction rules
- Make one small change per PR with a focused description and run tests
  locally before opening the PR. Include the commands you used to validate.
- If you need to change CI files, call out risks in the PR body and ask for
  a human review before merging.

---
If this file should be richer (for example, referencing specific code files or
build/test commands), please add the project files or tell me the repo path and
I will update this to reference concrete locations and commands.
