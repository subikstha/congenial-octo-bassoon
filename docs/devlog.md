# Devlog

## 2026-04-22 - Fix FastAPI router import and startup context

### Task
Fix `src/main.py` so the router import from `src/web/explorer.py` works reliably.

### Issue observed
- Running `python main.py` from inside `src/` failed with:
  - `ImportError: attempted relative import with no known parent package`
- Running `uvicorn src.main:app --reload` from inside `src/` failed with:
  - `ModuleNotFoundError: No module named 'src'`

### Root cause
- Relative imports require package context.
- Execution location (`web_layer/` vs `web_layer/src/`) changed module resolution.
- `web` package marker file was missing.

### Changes made
- Updated `src/main.py` to support both contexts:
  - Primary import: `from .web.explorer import router`
  - Fallback import: `from web.explorer import router`
- Updated router inclusion to `app.include_router(router)`.
- Added `src/web/__init__.py` (empty) to mark `web` as a package.
- Kept `uvicorn.run("main:app", reload=True)` in the script entrypoint for script-style execution.

### Verification
- From project root: `import src.main` succeeds.
- From `src/`: `import main` succeeds.
- Lint check on changed files: no errors.
