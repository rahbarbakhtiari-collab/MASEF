---
name: masef-wordpress-safety
description: Use for WordPress plugin work. Enforce the fixed MASEF WordPress factory policy, full engineering lifecycle, WordPress.org readiness, security, data safety, testing, packaging, and autonomous execution.
---

# WordPress Plugin Factory Workflow

1. Read `docs/00-governance/WORDPRESS-PLUGIN-FACTORY-POLICY.md` and `profiles/wordpress-plugin/PROFILE.md`.
2. Keep all engineering stages: product result, requirements, acceptance criteria, design, implementation, testing, review, packaging, deployment readiness, and post-release verification.
3. Use PHP `8.1+` and WordPress `7.2+`; do not add compatibility complexity for lower versions.
4. Build a Persian RTL interface with full internationalization, Text Domain equal to Slug, and safe LTR rendering.
5. Make meaningful product behavior configurable in the admin UI with sensible defaults; do not expose internal technical details as settings.
6. Use WordPress APIs instead of direct database access unless justified.
7. Validate and sanitize input, escape output, check capabilities and nonces, use `$wpdb->prepare()` for dynamic SQL, and protect direct file access.
8. Preserve data on deactivation and default uninstall. Provide an explicit, default-off option for complete data removal.
9. Do not add telemetry, hidden tracking, direct public-CDN loading, secrets in the repository, or unjustified production dependencies.
10. Prepare the plugin for WordPress.org from the first release: GPL-compatible licensing, standard English `readme.txt`, clean source, matching Slug/Text Domain, clean ZIP, and clear privacy behavior.
11. Test installation, activation, core behavior, access control, upgrade, deactivation, uninstall, RTL/LTR, and the installable ZIP.
12. Try LocalWP first, diagnose and repair reasonable environment failures, then use Docker if needed. Use strong substitute tests only when real WordPress execution is genuinely impossible and document the limitation.
13. Create meaningful Git commits, keep `main` healthy, prepare Tag and Release, and calculate SHA-256 for the final ZIP.
14. Do not deploy to Production or change real Production data. Deliver the installable package, evidence, and rollback instructions to the product owner.
15. Stop only for a true product ambiguity, unavailable secret/account action, new cost, irreversible data action, high-risk Production action, or explicit risk acceptance.
