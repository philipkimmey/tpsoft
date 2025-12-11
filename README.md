Product wedge and core workflow

Your wedge is: “Salesforce-familiar quoting + pricing consistency for foundation repair.”

Salesforce-familiarity matters most in:

Object names (“Leads”, “Accounts”, “Contacts”, “Opportunities”, “Quotes”)

Record pages + related lists (a familiar navigation pattern)

Statuses/stages (Lead Status, Opportunity Stage, Quote Status)

Ownership + activity tracking (Owner, Tasks/Activities, Notes/Files)

The end-to-end workflow you want to nail:

Lead captured (call/email/webform/import)

Convert → Account + Contact + Opportunity

Add Site/Inspection details (measurements/photos/notes)

Build Quote from a template/assembly + pricebook rules

Send PDF (and/or customer portal link) → revisions → accept

On acceptance: create Job/Project stub + deposit invoice (minimal finance hook)

That’s enough to be valuable without accidentally building a full ERP.

## Project setup

This repository now ships with a Django 6.0 starter configured for HTMX, uv-based dependency management, Docker, and Postgres. The goal is to provide a clean foundation for the specialty-contractor SaaS described above without implementing any business features yet.

### Local development with uv

1. Sync dependencies and create the virtual environment:

   ```bash
   uv sync
   ```

2. Apply the initial database migrations (uses SQLite by default unless Postgres environment variables are set):

   ```bash
   uv run python manage.py migrate
   ```

3. Start the development server:

   ```bash
   uv run python manage.py runserver
   ```

Visit http://127.0.0.1:8000 to see the landing page and a small HTMX interaction.

### Running with Docker Compose

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Build and start the services (web + Postgres):

   ```bash
   docker-compose up --build
   ```

The Django app will run at http://localhost:8000 and connect to the Postgres service defined in `docker-compose.yml`.

### Notes

- By default the application will use SQLite locally; providing `POSTGRES_*` variables (as in `.env.example`) switches the database configuration to Postgres.
- The Docker image uses uv for dependency installation to stay aligned with the local tooling.

MVP feature set for initial go-to-market
1) Salesforce-like CRM-lite (only what supports quoting)

Must-have

Leads: capture + status pipeline (New → Contacted → Scheduled → Qualified/Unqualified)

Accounts + Contacts (residential homeowners still fit: Account = “Household”)

Opportunities: stage pipeline, close date, expected value, owner

Basic search + list views + filters (think “Lead List View”, “Opportunity Pipeline”)

Nice soon (but not required)

Duplicate detection (phone/email/address)

Activity timeline (calls, SMS, emails)

Web-to-lead form

Why: you don’t want to require Salesforce to use your quote tool, but you do want it to feel familiar.

2) Estimating + quote builder designed for foundation repair

This is your acute pain point.

Must-have

Quote builder with:

Line items (qty, unit, unit price, discount, tax, totals)

Cost + margin (so they can protect profitability)

Sections/groups (“Scope”, “Mobilization”, “Permits”, “Warranty”, etc.)

Templates / “Assemblies”

E.g., “Push Piers – Standard”, “Helical Piers – Limited Access”, “Drainage Add-on”

Pre-built line groups + default quantities + formulas/inputs

Pricebook + product catalog

Standardized SKUs/services (per-pier, per-lf, mobilization, engineering letter, excavation)

Per-org pricing + ability to override on quote

Foundation-repair-specific edge

“Inspection inputs” that drive quantities:

Linear feet affected

Number of piers / spacing

Depth range

Access difficulty factor (multiplier)

Soil/engineering requirement flags

Store photos + annotated notes attached to the Opportunity/Inspection

This is the difference between “generic quoting” and “this was made for us.”

3) Quote document generation + versioning (critical)

Must-have

PDF quote output with company branding

Versioning (Quote v1, v2, v3)

“Sent/Presented” tracking (timestamp + who sent)

Expiration date + terms

Nice soon

Customer acceptance link (simple portal): “Accept quote” + capture name/email + timestamp (+ optional typed signature)

Optional alternates:

Base solution + Add-on(s)

“Option A: Push piers” vs “Option B: Helical piers”

This can be done as “Quote Line Groups” marked Optional

Versioning is non-negotiable: foundation quotes change after inspection discoveries and negotiation.

4) Minimal financial management entrypoint (don’t overbuild)

Must-have

Quote profitability summary:

Revenue, estimated cost, gross margin, margin %

Deposit request on acceptance (even if you don’t fully invoice)

Generate a “Deposit Invoice” record and mark as Unpaid/Paid manually

Nice soon

Invoice schedule (Deposit / Midpoint / Completion)

Payments tracking (manual entry or Stripe/ACH integration later)

Export to QuickBooks (CSV first; direct integration later)

This keeps you aligned with your “bid and financial management” entrypoint without building full accounting.

5) Roles, permissions, and audit trail (small but essential in B2B SaaS)

Must-have

Roles: Admin, Sales/Estimator, Manager (approve discounts), Finance (invoices)

Audit basics: created_by / updated_by, timestamps

Field history (at least for stage/status, totals, discount)

In construction sales orgs, discounting and quote edits are sensitive.
