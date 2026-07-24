#!/usr/bin/env python3
"""Create an execution plan from the MASEF template."""
from pathlib import Path
import argparse, re

ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    value = value.strip().lower().replace(' ', '-')
    return re.sub(r'[^a-z0-9-]+', '', value) or 'plan'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', required=True, help='Example: 001')
    parser.add_argument('--title', required=True)
    parser.add_argument('--slug', default='')
    args = parser.parse_args()

    template = ROOT / 'docs/05-execution/plans/active/PLAN-TEMPLATE.md'
    slug = args.slug or slugify(args.title)
    target = template.parent / f'PLAN-{args.id}-{slug}.md'
    if target.exists():
        raise SystemExit(f'Plan already exists: {target}')
    text = template.read_text(encoding='utf-8').replace('PLAN-XXX — عنوان', f'PLAN-{args.id} — {args.title}', 1)
    target.write_text(text, encoding='utf-8')
    print(target.relative_to(ROOT))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
