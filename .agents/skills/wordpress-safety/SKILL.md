---
name: masef-wordpress-safety
description: Use for WordPress, WooCommerce, LearnDash, Elementor, themes, or plugins. Enforce WordPress security, compatibility, data migration, staging, backup, and rollback rules. Do not modify production directly.
---

# WordPress Safety Workflow

- Confirm WordPress, PHP, database, plugin, and theme versions.
- Use WordPress APIs instead of direct database access unless justified.
- Validate and sanitize input; escape output at render time.
- Check capabilities and nonce for state-changing admin/AJAX/REST actions.
- Use `$wpdb->prepare()` for dynamic SQL.
- Prefix options, transients, hooks, classes, and tables.
- Provide activation, deactivation, uninstall, migration, and rollback behavior.
- Test on staging with backup before production.
- Preserve compatibility with active caching and security layers.
