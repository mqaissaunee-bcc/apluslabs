# A+ Lab Companion

Student companion pages for all 18 labs in the NDG **CompTIA A+ Lab Series v4** (Labs 01-A through 17), mapped to the current A+ exams: 220-1201 (Core 1) and 220-1202 (Core 2). Each page is a single self-contained HTML file with no external scripts or fonts. Pages are CSP-safe for Canvas embedding and work offline.

## What each lab page includes

- Why the lab matters, and the lab machines and logins
- **Then vs. now:** where each Windows 7/8.1/10 step lives on Windows 11
- A step-by-step walkthrough with screenshot markers, copy buttons on commands, and "where people get stuck" callouts, including corrections for typos in the source PDFs
- Reference tables for the tools and commands, beyond what the lab uses
- A troubleshooting table, help desk scenarios, and A+ exam relevance
- Self-check questions, an evidence (screenshot) checklist, and a printable cheat sheet
- Light/dark mode, text size, print, and progress tracking saved in the browser

## Files

- `index.html` is the lab home. It has sorting, Core 1 / Core 2 filters, and each student's progress per lab.
- `aplus_lab01a_companion.html` through `aplus_lab17_companion.html` are one page per lab.
- `tools/` holds the build:
  - `tools/bodies/labNN.txt` holds each lab's content in a short markup format (see `tools/markup.py`). Lab 01-A is in HTML.
  - `tools/shell.py` holds the shared design, header, and scripts.
  - `tools/labs.py` holds lab titles, tools, and exam mapping.

To rebuild after editing: `cd tools && python3 build.py`, then copy `tools/site/*.html` to the repository root.

## Credits

Built for CompTIA A+ hands-on practice at Brookdale Community College. Open educational resource. Independent of and not endorsed by CompTIA or Network Development Group. CompTIA A+ is a registered trademark of CompTIA, Inc.
