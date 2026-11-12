# Configuration Status Accounting (CSA) Report

**Project:** sen401-inventory-csa
**Author:** Temidayo Omoyajowo (2025/B/SENG/0513)
**Repository:** `temidayo-sen401/sen401-inventory-csa` (private)
**Date:** 2026-11-12

Configuration Status Accounting records **what** changed in the project,
**who** changed it, **when**, **why**, and **which baseline** it belongs to. In
this project Git is the system of record: every change is a commit, branches
separate stable work from in-progress work, and tags mark released baselines.

## 1. Configuration items (CIs) in baseline v1.0

| Configuration item | Type | Description |
|--------------------|------|-------------|
| `inventory.py` | Source | Inventory data (`item_name`, `quantity`, `price`) and the CSV export |
| `app.py` | Source | Entry point that prints the stock report |
| `utils/helpers.py` | Source | Pure helper functions (stock value, highest/lowest, low stock) |
| `tests/test_helpers.py` | Test | `unittest` suite for the helpers |
| `requirements.txt` | Config | Dependencies (standard library only; Python 3.12+) |
| `.python-version` | Config | Pins the Python runtime to 3.12 |
| `.gitignore` | Config | Excludes caches, virtual environments and generated `inventory.csv` |
| `README.md` | Docs | Project description and usage |
| `changelog.txt` | Docs | Generated commit log (added after v1.0) |

## 2. Branches

| Branch | Role | Status |
|--------|------|--------|
| `main` | Stable, release-ready code | Contains baseline v1.0 plus `changelog.txt` |
| `dev` | Maintenance and development work | All four maintenance commits; merged into `main` with `--no-ff` |

## 3. Releases / baselines

| Tag | Commit | Date | Contents |
|-----|--------|------|----------|
| `v1.0` | `8d22378` | 2026-11-12 | Inventory app after corrective, adaptive, perfective and preventive maintenance |

## 4. Change record: commits mapped to maintenance tasks

| # | Commit | Branch | Maintenance type | Change | Files |
|---|--------|--------|------------------|--------|-------|
| 0 | `2ecab0a` | main | Initial version | Starter inventory app | all source files |
| 1 | `881ab8b` | dev | **Corrective** | Total stock value used `quantity + price` instead of `quantity * price` (₦807,310 vs ₦10,522,500). `lowest_stock_item` started from 0, so it always returned `None`. | `app.py`, `utils/helpers.py` |
| 2 | `0b3ace3` | dev | **Adaptive** | Targets Python 3.12 (PEP 695 `type` alias, `X \| None` hints, `.python-version`); new feature: CSV export with the `csv` module | `inventory.py`, `utils/helpers.py`, `app.py`, `requirements.txt`, `.python-version`, `.gitignore` |
| 3 | `c424d74` | dev | **Perfective** | Formatted stock report with per-item value, thousands separators and low-stock alerts | `app.py`, `utils/helpers.py` |
| 4 | `2000330` | dev | **Preventive** | Split `app.py` into functions with a `main()` guard, simplified helpers, added docstrings, a named threshold constant and unit tests | `app.py`, `utils/helpers.py`, `tests/`, `README.md` |
| 5 | `8d22378` | main | Integration | Merge `dev` into `main`; tagged **v1.0** | — |
| 6 | `ca80ea3` | main | Documentation | Generated `changelog.txt` | `changelog.txt` |

## 5. Commands used for status accounting

| Purpose | Command |
|---------|---------|
| Commit history | `git log --oneline` |
| Branch/merge structure | `git log --graph --all --decorate --oneline` |
| Branch inventory | `git branch -a` |
| Release inventory | `git tag -n`, `git show v1.0 --stat --no-patch` |
| Change log with author and date | `git log --all --pretty=format:"%h \| %an \| %ad \| %s" --date=format:"%Y-%m-%d %H:%M" > changelog.txt` |
| Files in a baseline | `git ls-tree -r --name-only v1.0` |
| Changes between versions | `git diff --stat 2ecab0a v1.0` |

## 6. Configuration audit (v1.0)

| Check | Type | Result |
|-------|------|--------|
| Every CI in section 1 exists at tag `v1.0` (`git ls-tree`) | Physical | Pass |
| No generated or secret files are committed (`inventory.csv`, `.venv`, caches) | Physical | Pass |
| Total stock value = ₦10,522,500 (hand-checked: sum of quantity × price) | Functional | Pass |
| Lowest stock item = Printer (5); highest = USB Flash Drive (150) | Functional | Pass |
| `python3.12 -m unittest` passes (5 tests) | Functional | Pass |
| Each maintenance commit has one purpose and a descriptive, typed message | Process | Pass |

## 7. Observations

- **Traceability:** Using one commit per maintenance type, with a prefix
  (`fix(corrective)`, `feat(adaptive)`, ...), means each change can be traced
  straight to its purpose with `git log --oneline`. No external tool is needed.
- **Branch isolation:** All maintenance happened on `dev`, so `main` was never in
  a half-finished state. The `--no-ff` merge keeps that history visible in
  `git log --graph`.
- **Baselines:** The annotated tag `v1.0` freezes an exact, reproducible state
  (`git checkout v1.0`) that later work can be compared with.
- **Automatic records:** Git stores the author, timestamp and content hash of
  every commit, so `changelog.txt` is generated from the history rather than
  written by hand, and it cannot drift from what actually happened.
- **Limitation:** Generating the change log copies history at one moment; it has to
  be regenerated (or automated in CI) after new commits.
