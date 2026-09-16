# CLAUDE.md

## Project overview

Static GitHub Pages knowledge base for Vibe Coding Bootcamp notes, practical AI-assisted development guidance, QA checklists, prompts, and examples.

## Technical constraints

- Static HTML, CSS, and vanilla JavaScript only.
- No build step and no server-side runtime.
- The production entry point is `/index.html`.
- Use relative paths for local assets.
- The site must remain compatible with GitHub Pages.
- Do not add dependencies unless explicitly requested.

## Working rules

1. Inspect the current implementation before editing.
2. Present a short implementation plan before changes that affect multiple sections.
3. Make one logical change at a time.
4. Preserve existing content unless removal is explicitly requested.
5. Never disable validation or delete content merely to make a check pass.
6. Keep all user-facing content in Russian unless requested otherwise.
7. Do not add secrets, tokens, credentials, or private URLs to the repository.
8. Keep external links explicit and safe (`target="_blank"` with `rel="noopener noreferrer"`).

## Quality requirements

- Semantic HTML and correct heading hierarchy.
- Keyboard-accessible interactive controls.
- Visible focus states and readable contrast.
- Responsive layout at 375px and 1280px widths.
- No horizontal overflow on mobile.
- JavaScript must not throw errors when storage or clipboard APIs are unavailable.
- Escape user-entered content before inserting it into the DOM.

## Definition of done

- [ ] Page opens without console errors.
- [ ] Navigation links work.
- [ ] Copy buttons work or fail gracefully.
- [ ] Custom note add/delete flow works.
- [ ] Layout is usable on mobile and desktop.
- [ ] No credentials or generated secrets are committed.
- [ ] Changes are summarized with affected files and checks performed.
