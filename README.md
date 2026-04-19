Build a Testable Todo Item Card

Concept
Build a clean, modern Todo / Task Card component (or a small page containing one card).

Required Content & Exact data-testid Values
:warning: These must match exactly for automated tests.

Root card container → data-testid="test-todo-card"
Task title (e.g., h2 or h3) → data-testid="test-todo-title"
Task description / notes (paragraph or div) → data-testid="test-todo-description"
Priority badge/label → data-testid="test-todo-priority"
Must show one of: Low, Medium, High (or emoji/icons representing them)

Due date / deadline (formatted nicely, e.g. "Due Feb 18, 2026") → data-testid="test-todo-due-date"
Current time remaining hint → data-testid="test-todo-time-remaining"
Example values:
"Due in 3 days"
"Due tomorrow"
"Overdue by 2 hours"
"Due now!"

Updates roughly every 30–60 seconds (or at least shows correct initial value)

Status indicator (e.g., "Pending" / "In Progress" / "Done") → data-testid="test-todo-status"
Checkbox or toggle for completion → data-testid="test-todo-complete-toggle"
Must be a real <input type="checkbox"> or properly labeled button with role="checkbox"

Tags / categories list (chips/pills) → data-testid="test-todo-tags"
Each tag can optionally have:
data-testid="test-todo-tag-work"
data-testid="test-todo-tag-urgent"


"Edit" button/icon → data-testid="test-todo-edit-button"
"Delete" button/icon → data-testid="test-todo-delete-button"


HTML & Semantics Recommendations
Use proper semantic HTML:
• Card root → <article> or <section role="region">
• Title → <h2> or <h3>
• Description → <p>
• Priority & Status → <span> or <strong>

Add aria-label if visual-only
• Due date & time-remaining → <time> element (with datetime attribute if possible)
• Checkbox → real <input type="checkbox"> + <label>
• Tags → <ul role="list"> of <li>
OR <div role="list"> with chips
• Buttons → <button> (not <div>)

Add aria-label if icon-only


Accessibility Requirements
• Checkbox must have:
• A visible label
OR
• aria-label / aria-labelledby
• All buttons must have accessible names (visible text or aria-label)
• Priority / status badges should have aria-label if they are purely visual
• Good color contrast (WCAG AA compliant)
• Focus styles must be visible
• Fully keyboard navigable:

Tab → checkbox → edit → delete
• If time-remaining updates live:

Consider wrapping it in aria-live="polite"
Or skip live updates for simplicity in Stage 0


Responsiveness Requirements

Mobile:
Full-width card
Stacked vertical layout

Tablet/Desktop:
Comfortable max-width (420–500px recommended)
Good padding and spacing

Tags should wrap nicely (flex-wrap)
No horizontal overflow at any screen width
Should look correct from 320px to 1200px


Behaviour / Implementation Guidance

Hard-code 1–3 example tags (e.g., work, urgent, design)
Hard-code one initial:
Priority
Status
Due date

Time Remaining
• Calculate from:
• A fixed due date (e.g., March 1, 2026 18:00 UTC)
OR
• Date.now() + offset
• Show friendly text:

"Due in 3 days"
"Due tomorrow"
"Overdue by 2 hours"
"Due now!"
• Optional:

Refresh every ~60 seconds with setInterval
Not required for Stage 0
Checkbox Toggle Behaviour
When toggled:

Visually update the card:
Strike-through title
Change status to "Done"

Edit & Delete Buttons

Can be dummy actions:
console.log("edit clicked")
alert("Delete clicked")



Acceptance Criteria (Grading / Auto-Tests)

All required data-testid elements exist and are visible
Checkbox is:
Focusable
Toggleable via keyboard
Screen-reader accessible

Time-remaining shows reasonable value (± few minutes tolerance)
Edit & Delete buttons are:
Present
Keyboard-focusable

Semantic HTML used correctly:
article/section
time
label
button
list

Responsive layout works properly (320px–1200px)
No layout shift or horizontal overflow with long text
Priority & status are clearly displayed


This task keeps the focus on:

Testability
Accessibility
Responsiveness

STAGE 1A TASK
rontend Wizards — Stage 1a Task
Advanced Todo Card (Interactive & Stateful)

Overview:
In Stage 1, you will extend your Stage 0 Todo Card into a more interactive, stateful, and slightly more “app-like” component. You are still building a single Todo Card, not a full app. The card should now support:


Editable content
Status transitions
Priority changes
Expand / collapse behavior
More dynamic time handling
Slightly richer accessibility patterns


:new: Enhancements: Add the following functionality:


Editing mode: When the edit button is clicked, the card should enter edit mode.
Edit form container → data-testid="test-todo-edit-form"
Title input → data-testid="test-todo-edit-title-input"
Description textarea →data-testid="test-todo-edit-description-input"
Priority select dropdown → data-testid="test-todo-edit-priority-select"
Due date input → data-testid="test-todo-edit-due-date-input"
Save button → data-testid="test-todo-save-button"
Cancel button → data-testid="test-todo-cancel-button"




Status Controls: Instead of just displaying status, allow the user to toggle it.
Add: 
Status dropdown or segmented control → data-testid="test-todo-status-control"

Allowed statuses: "Pending" , "In Progress"  and "Done"




Priority Indicator Enhancements: 
Add:
Priority indicator → data-testid="test-todo-priority-indicator"

This could be:
A colored dot
An icon
A left border accent
Background color change

It must visually change depending on: "Low" , "Medium" , "High"




Expand / Collapse Behavior: The description should be collapsible if it's too long.
Add:
Expand/collapse toggle button → data-testid="test-todo-expand-toggle"
Collapsible container → data-testid="test-todo-collapsible-section"

Behavior:
Default collapsed if description exceeds certain length
Clicking expand reveals full content
Toggle must be keyboard accessible





Time Management Enhancements
Add:
Overdue indicator → data-testid="test-todo-overdue-indicator"

If overdue:
Show a visible visual change (e.g., red text or badge)
Show explicit "Overdue" indicator

Time logic should now:
Update every 30–60 seconds
Show granular time: "Due in 2 days" , "Due in 3 hours" , "Due in 45 minutes" , "Overdue by 1 hour"

If status becomes "Done":
Time remaining should stop updating
Replace with: "Completed"






:dart: Behavioral Requirements: 

1. Edit Mode

Clicking Edit switches into edit form
Save updates the card values
Cancel restores previous values
Edit mode must:
Trap focus inside form (optional bonus)
Return focus to Edit button when closed


2. Status Logic Rules

If checkbox toggled → status becomes "Done"
If status manually set to "Done" → checkbox becomes checked
If unchecked after "Done"→ revert to "Pending"
Status must stay visually synced with: Checkbox , Status display  and Status control


3. Visual State Changes

"Done" → strike-through title + muted colors
"High priority" → strong visual indicator
"Overdue" → red accent
"In Progress" → distinct visual style


:wheelchair: Accessibility Requirements:


Edit form fields must have <label for="">
Status dropdown must have accessible name
Expand toggle must use: aria-expanded , aria-controls
Collapsible section must have matching id
Live time updates should use aria-live="polite"



Keyboard flow must remain: Tab →
Checkbox
Status control
Expand toggle
Edit
Delete
Save/Cancel (in edit mode)



:iphone: Responsiveness 

Layout adapts to:

320px mobile
768px tablet
1024px+

Edit form fields stack vertically on mobile
On desktop:

Priority & status may align horizontally

No layout breaking when:

Title is long
Tags wrap to multiple lines
Description is extremely long


:test_tube:  Acceptance Criteria

All Stage 0 testids still exist
All new testids exist and work
Edit mode fully functional
Status transitions synchronized
Expand/collapse accessible
Overdue logic correct
No visual overflow at any size
Keyboard fully usable
Time updates properly
Clean state management




:package: Submission

Updated Live URL
Updated GitHub repo
Updated README including:

What changed from Stage 0
New design decisions
Any known limitations
Accessibility notes


STAGE 1B TASK
Frontend Wizards — Stage 1B Task: Build a Testable Profile Card

In this task, you’ll build a small, accessible, responsive Profile Card component/page using semantic HTML and modern frontend patterns (React is recommended but plain HTML/CSS/vanilla JS is fine). Every visible element must include a data-testid attribute so automated tests can target it.

Study material (recommended)

HTML semantics & accessibility: 
Accessible images & alt text: 


Task — Profile Card (core requirements)

Required content (each item must exist and include the specified data-testid)


Profile card root container — data-testid="test-profile-card"
Name (plain text) — data-testid="test-user-name"
Short biography (paragraph) — data-testid="test-user-bio"
Current time (in milliseconds) — data-testid="test-user-time"

The component should show the current epoch time in milliseconds at render or update.

Avatar image (user photo) — data-testid="test-user-avatar"
Social links list (one element containing the links) — data-testid="test-user-social-links"

Each link item may have data-testid="test-user-social-<network>" (e.g. "test-user-social-twitter")

Hobbies (list) — data-testid="test-user-hobbies"
Dislikes (list) — data-testid="test-user-dislikes"


All data-testid attributes are required exactly as shown so tests are stable.

HTML & semantics:  Example suggestions:

Wrap the card in <article> ("test-profile-card")
Name inside a <header> or an <h2> with aria-label as needed
Bio in a <p>
Avatar inside a <figure> with <img> and <figcaption> (if caption used)
Social links inside a <nav> or <ul>
Hobbies/dislikes each inside <section> and presented as <ul>/<li>
All interactive items (links/buttons) must be keyboard-focusable.


Accessibility requirements:

Provide meaningful alt text for the avatar image.
Ensure color contrast meets WCAG AA for text.
All form-like or interactive elements must have accessible names.
Provide aria-live or similar if time updates dynamically (so screen readers can be notified OR ensure time is announced on demand).
Keyboard navigation: user must be able to tab through the card, focus each link, and activate them.


Responsiveness

Card must look good on mobile, tablet, and desktop.
On small screens, stack content vertically; on wider screens, arrange avatar to the left and text to the right (or any clean layout).
Use CSS that doesn’t break layout when content length changes (word-wrap, truncation with accessible expansion, etc.)


Behavior / Implementation guidance

The time in milliseconds should be accurate and reflect Date.now() at render or on an update tick (if you choose to update it, do so reasonably — e.g., refresh every 500–1000ms).
Avatar should accept either a URL or an uploaded image (if upload used, the component must ultimately display an image URL).
Social links should open in a new tab (target="_blank") with rel="noopener noreferrer".
Use semantic markup and modern CSS (Flexbox or Grid).


Acceptance criteria (checklist for grading / automated tests)

All required elements exist and are discoverable by the given data-testids.
HTML uses semantic tags (article, figure, nav, section, headings).
The test-user-time value equals Date.now() (or a value within a reasonable delta if rendering delay exists) and is shown in milliseconds.
Avatar renders with an alt attribute and data-testid="test-user-avatar".
Social links present inside test-user-social-links and optionally individually testable (e.g., test-user-social-twitter).
Hobbies and dislikes are distinct lists with their respective data-testids.
Keyboard navigation works for links; focus styles are visible.
Layout is responsive at typical breakpoints (mobile/tablet/desktop).
