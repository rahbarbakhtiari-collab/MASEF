---
name: masef-wordpress-safety
description: Use for WordPress, WooCommerce, LearnDash, Elementor, themes, or plugins. Apply WordPress security and compatibility controls in proportion to the actual change and avoid unnecessary hosting or approval gates.
---

# WordPress Safety Workflow

- Use WordPress APIs instead of direct database access unless justified.
- Validate and sanitize input; escape output at render time.
- Check capabilities and nonce for state-changing admin/AJAX/REST actions.
- Use `$wpdb->prepare()` for dynamic SQL.
- Prefix options, transients, hooks, classes, and tables.
- Define activation, deactivation, uninstall, migration, and rollback only where relevant.
- For a light plugin without schema or sensitive data, test the installable ZIP and use deactivate/delete as the normal rollback.
- Inspect exact environment details only when compatibility depends on them or a real error appears.
- Align minimum PHP and WordPress versions with the destination when technically safe instead of forcing infrastructure upgrades.
- Staging, full backup, restore rehearsal, cache analysis, and independent review are required only for standard or critical changes.
- Stop before production only when the action has meaningful data, availability, security, or business risk.
