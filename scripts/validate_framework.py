#!/usr/bin/env python3
"""Validate the minimum MASEF repository structure without external dependencies."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'AGENTS.md',
    'docs/00-governance/PROJECT-CHARTER.md',
    'docs/00-governance/RISK-PROFILE.md',
    'docs/00-governance/QUALITY-GATES.md',
    'docs/00-governance/WORDPRESS-PLUGIN-FACTORY-POLICY.md',
    'docs/01-product/REQUIREMENTS.md',
    'docs/01-product/ACCEPTANCE-CRITERIA.md',
    'docs/03-architecture/ARCHITECTURE.md',
    'docs/04-security/SECURITY.md',
    'docs/04-security/THREAT-MODEL.md',
    'docs/05-execution/plans/active/PLAN-TEMPLATE.md',
    'docs/06-quality/TEST-STRATEGY.md',
    'docs/07-operations/DEPLOYMENT.md',
    'docs/07-operations/ROLLBACK.md',
    'docs/08-evidence/EVIDENCE-PACK-TEMPLATE.md',
    'profiles/wordpress-plugin/PROFILE.md',
    '.github/workflows/framework-check.yml',
]

FORBIDDEN_PATTERNS = [
    'sk-proj-',
    'BEGIN PRIVATE KEY',
    'password = "',
    "password = '",
]

WORDPRESS_POLICY_MARKERS = [
    'PHP: `8.1`',
    'WordPress: `7.2`',
    'رهبر بختیاری',
    'GPL-2.0-or-later',
    'Telemetry',
    'حذف کامل تنظیمات و داده‌ها هنگام حذف افزونه',
]


def main() -> int:
    errors = []
    for rel in REQUIRED:
        p = ROOT / rel
        if not p.is_file():
            errors.append(f'MISSING: {rel}')
        elif p.stat().st_size < 40:
            errors.append(f'TOO SMALL: {rel}')

    version_path = ROOT / 'VERSION'
    manifest_path = ROOT / 'manifest.json'
    if version_path.is_file() and manifest_path.is_file():
        version = version_path.read_text(encoding='utf-8').strip()
        try:
            manifest_version = json.loads(manifest_path.read_text(encoding='utf-8'))['version']
        except (json.JSONDecodeError, KeyError) as exc:
            errors.append(f'INVALID manifest.json: {exc}')
        else:
            if version != manifest_version:
                errors.append(f'VERSION MISMATCH: VERSION={version}, manifest={manifest_version}')

    policy_path = ROOT / 'docs/00-governance/WORDPRESS-PLUGIN-FACTORY-POLICY.md'
    if policy_path.is_file():
        policy = policy_path.read_text(encoding='utf-8')
        for marker in WORDPRESS_POLICY_MARKERS:
            if marker not in policy:
                errors.append(f'WORDPRESS POLICY MARKER MISSING: {marker}')

    for p in ROOT.rglob('*'):
        if (
            not p.is_file()
            or p.resolve() == Path(__file__).resolve()
            or p.name == 'manifest.json'
            or '.git' in p.parts
            or p.suffix in {'.zip', '.png', '.jpg'}
        ):
            continue
        try:
            text = p.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in text:
                errors.append(f'POTENTIAL SECRET in {p.relative_to(ROOT)}: {pattern}')

    if errors:
        print('MASEF validation failed:')
        for err in errors:
            print(f' - {err}')
        return 1

    print(f'MASEF validation passed. Required files: {len(REQUIRED)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
