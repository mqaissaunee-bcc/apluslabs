# A+ Lab Companion: PDF reconciliation report

Every companion page was checked against the full text of its NDG CompTIA A+ Lab Series v4 PDF (document version 2020-12-14), one lab at a time.

## How it was checked

1. **Full text.** Each PDF's complete text was extracted, page by page (18 PDFs, 578 pages, none encrypted or image-only). That text was diffed against the condensed view used to write the original pages. The diff found that the original build had hidden three step lines: every line containing "netdevgroup" was dropped along with the footer. All three are restored (Lab 09 twice, Lab 12 once).
2. **Steps.** Each PDF section's numbered steps were compared with the companion walkthrough. Each task heading now shows the PDF section it covers.
3. **Command check.** The check extracted:
   - every command the PDF shows at a prompt (`C:\...>`, `PS C:\...>`, `sysadmin@lubuntu:...$`)
   - every value students type into a Run box, search box, file dialog, or the Registry
   - every line of the three Lab 17 scripts

   En dashes and curly quotes were converted to straight characters. Each item had to appear in the companion's walkthrough: prompt commands and script lines in a command block, typed values anywhere in the walkthrough text. **Result: 271/271 matched.** No real gaps remain. GUI-only steps have nothing to type and are covered by step text.
4. **Machine-attribution check.** Every command block was checked against the machine band (or inline label) it sits under: Linux prompts only under Lubuntu or New-Lubuntu, Windows prompts only under Windows machines, and nothing outside a band. **Result: 0 issues.**
5. **Structure and browser.** All 19 pages:
   - have balanced HTML tags
   - have no inline event handlers, no duplicate IDs, and no broken internal links
   - make no external requests
   - pass in a browser: no script errors, no sideways scrolling at 390 px, and theme, progress, and Copy all work (Copy leaves out prompts)

## Per-lab results

| Lab | PDF prompt commands | Script lines | Typed entries | Matched | Command blocks | Machine bands | Status |
|---|---|---|---|---|---|---|---|
| Lab 01-A Examining PC Hardware (BIOS/UEFI, Device Manager) | 0 | 0 | 1 | 1/1 | 1 | 4 | Matched |
| Lab 01-B Examining PC Hardware (System Information) | 4 | 0 | 6 | 10/10 | 5 | 7 | Matched |
| Lab 02 Windows Management and Administrative Tools | 0 | 0 | 11 | 11/11 | 5 | 7 | Matched |
| Lab 03 Windows Network Settings | 14 | 0 | 2 | 16/16 | 8 | 5 | Matched |
| Lab 04 Windows Users and Groups | 0 | 0 | 8 | 8/8 | 2 | 6 | Matched |
| Lab 05 Sharing Resources: Folders | 0 | 0 | 9 | 9/9 | 1 | 7 | Matched |
| Lab 06 Sharing Resources: Printers | 0 | 0 | 4 | 4/4 | 1 | 3 | Matched |
| Lab 07 Disk Maintenance and Data Recovery | 2 | 0 | 7 | 9/9 | 2 | 7 | Matched |
| Lab 08 Command Line: Windows and Linux | 65 | 0 | 0 | 65/65 | 18 | 3 | Matched |
| Lab 09 Windows Control Panel | 0 | 0 | 3 | 3/3 | 2 | 7 | Matched |
| Lab 10 Windows Customizations | 0 | 0 | 1 | 1/1 | 0 | 4 | Matched |
| Lab 11 Remote Access | 0 | 0 | 8 | 8/8 | 6 | 7 | Matched |
| Lab 12 Troubleshooting Tools in Windows | 4 | 0 | 12 | 16/16 | 8 | 8 | Matched |
| Lab 13 Installing Software | 5 | 0 | 4 | 9/9 | 4 | 3 | Matched |
| Lab 14 Managing Storage | 0 | 0 | 4 | 4/4 | 0 | 2 | Matched |
| Lab 15 Security and Privacy | 8 | 0 | 10 | 18/18 | 9 | 11 | Matched |
| Lab 16 Deploy a Virtual Machine with Hyper-V | 2 | 0 | 8 | 10/10 | 3 | 5 | Matched |
| Lab 17 Writing Basic Scripts | 12 | 51 | 6 | 69/69 | 12 | 3 | Matched |

## What changed, lab by lab

- **Lab 01-A Examining PC Hardware (BIOS/UEFI, Device Manager).** Converted from hand-written HTML to the shared build format. Bands added (Win7, Win10, Win7, Win10). The `shutdown /r /o` and `/fw` commands are not in the PDF and are now labeled as optional extras.
- **Lab 01-B Examining PC Hardware (System Information).** Added the missing `exit` steps and the sign-in steps on each machine. Applied the PDF's `C:\Windows\System32>` prompt, with a note that a prompt opened from Run usually starts in the user folder. Bands added for 5 machine switches.
- **Lab 02 Windows Management and Administrative Tools.** Typed entries (Run box, Start search, file names, the registry key) are now shown as labeled commands. Added a note that the PDF's step numbering skips 18 and 23 to 26 in section 5.1; no content is missing.
- **Lab 03 Windows Network Settings.** Added the missing `net use /?` (step 12). Flagged the PDF's `C:\User\sysadmin>` prompt typo. Confirmed that section 4 runs on Win10. Curly quotes in `net use *` are converted to straight quotes.
- **Lab 04 Windows Users and Groups.** Bands added. `gpedit.msc` and the RSAT `.msu` file are shown as commands. Sign-out and sign-in sequences are spelled out per the PDF.
- **Lab 05 Sharing Resources: Folders.** Split a step that combined Win8.1 and Win10 into separately banded steps. The final step switches machines partway through, so it now uses inline labels.
- **Lab 06 Sharing Resources: Printers.** Bands added. The printer path is shown as a command, and the environment text was updated to say which machine hosts and which connects.
- **Lab 07 Disk Maintenance and Data Recovery.** Moved the backup check from the Win10 band to its own Win8.1 band (it runs on Win8.1). Applied the exact prompt change after `cd`.
- **Lab 08 Command Line: Windows and Linux.** Rebuilt all 65 commands in PDF order with the exact prompt for each, including every prompt change after `cd`. Restored the `dir` checks between file operations that the page had condensed.
- **Lab 09 Windows Control Panel.** Restored two steps the original build hid: setting the Home page and adding the Trusted Sites address, both `https://www.netdevgroup.com/`. An optional `winver` command is now labeled as an extra.
- **Lab 10 Windows Customizations.** Bands added.
- **Lab 11 Remote Access.** Bands show which console the student sits at. Inline labels mark actions inside the RDP session (Win10 to Win7, then Win7 to Win10). Computer, Remote Host, and file entries are shown as commands.
- **Lab 12 Troubleshooting Tools in Windows.** Restored the missing Firefox step (section 1.8, step 4: `www.netdevgroup.com`). Typed paths are shown as commands and the `sfc` and DISM prompts applied. Added a note that the PDF repeats step numbers 4 to 5 in section 1.7.
- **Lab 13 Installing Software.** Applied the exact Lubuntu prompts, including the prompt change after each `cd`. Added `exit`. `dpkg –i` is shown corrected to `-i`, and the CPU-Z path corrected to `Program Files`.
- **Lab 14 Managing Storage.** Bands and PDF tags added. Added a note that step 9's text says "Size (minimum)" while the screen field is labeled "Size (maximum)".
- **Lab 15 Security and Privacy.** Task 5 is split into banded runs; one command block had mixed Win10 and Win7 pings. Applied the `C:\Users\sysadmin>` and `PS C:\Windows\system32>` prompts and added the closing `exit`. Kept the note that the PDF's step 17 has the ping result backwards. `manage-bde –status` is shown corrected to `-status`.
- **Lab 16 Deploy a Virtual Machine with Hyper-V.** `-FeatureName:Microsoft-Hyper-V` now matches the PDF exactly (with the colon). Added a New-Lubuntu band for the install inside the nested VM, and the PDF's ISO path with a note that its file name appears truncated.
- **Lab 17 Writing Basic Scripts.** Fixed a build bug that had deleted the batch file's first line (`@ECHO OFF`), so the page now matches the PDF; the page delivered earlier was missing that line. Restored the exact text of the long `rem` line. Script files are shown in captioned file blocks, separate from prompt commands. Prompts applied, with a note that the PDF's prompt text differs from its screenshots.

## Applies to all pages

- **Lab Settings.** The Environment section shows the PDF's Lab Settings table exactly as printed, plus a pod topology diagram. Machines the PDF lists but no step uses (or only the optional challenge tasks use) are marked.
- **Prompts.** Every command shows its PDF prompt; prompts can't be selected and are left out of Copy. Commands typed into dialogs carry a label instead, such as "Run box:" or "File name:".
- **Machine bands.** "On Win7 / Win8.1 / Win10 / Lubuntu / New-Lubuntu" bands mark each run of steps; inline labels mark a switch partway through a step.
- **Screenshots.** None of these PDFs requires a screenshot. The capture markers and evidence checklists on every page are added by this companion.
- **Safety.** No content was withheld. These are administration labs with no offensive techniques.
- **Currency.** Notes cover deprecated tools: WMIC, `Get-WmiObject` (use `Get-CimInstance`), PowerShell ISE, Steps Recorder, Disk Cleanup, Internet Explorer, and dynamic disks. The pages still use what each lab uses.
