#!/usr/bin/env python3
"""Create a new project repository from the MASEF template."""
from pathlib import Path
import argparse
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDES = {'.git', '__pycache__'}


def copy_tree(src: Path, dst: Path) -> None:
    for item in src.iterdir():
        if item.name in EXCLUDES or item.name.endswith('.zip'):
            continue
        target = dst / item.name
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            copy_tree(item, target)
        else:
            shutil.copy2(item, target)


def main() -> int:
    parser = argparse.ArgumentParser(description='Bootstrap a MASEF project')
    parser.add_argument('--name', required=True, help='Human-readable project name')
    parser.add_argument('--slug', required=True, help='English project slug')
    parser.add_argument(
        '--profile',
        action='append',
        dest='profiles',
        choices=['generic', 'wordpress-plugin', 'webapp', 'api-service'],
        help='Repeat to combine technical profiles',
    )
    parser.add_argument(
        '--risk',
        choices=['light', 'standard', 'critical'],
        default='light',
        help='Execution mode; defaults to light',
    )
    parser.add_argument('--output', required=True, help='Target directory')
    args = parser.parse_args()

    out = Path(args.output).expanduser().resolve()
    if out.exists() and any(out.iterdir()):
        print(f'ERROR: target directory is not empty: {out}', file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)
    copy_tree(ROOT, out)

    charter = out / 'docs/00-governance/PROJECT-CHARTER.md'
    text = charter.read_text(encoding='utf-8')
    text = text.replace('- نام پروژه:', f'- نام پروژه: {args.name}', 1)
    text = text.replace('- نام کوتاه/Slug:', f'- نام کوتاه/Slug: {args.slug}', 1)
    text = text.replace('- حالت اجرا: `light | standard | critical`', f'- حالت اجرا: `{args.risk}`', 1)
    charter.write_text(text, encoding='utf-8')

    risk_profile = out / 'docs/00-governance/RISK-PROFILE.md'
    risk_text = risk_profile.read_text(encoding='utf-8')
    risk_text = risk_text.replace(
        '- حالت اجرا: `light | standard | critical`',
        f'- حالت اجرا: `{args.risk}`',
        1,
    )
    risk_profile.write_text(risk_text, encoding='utf-8')

    profiles = args.profiles or ['generic']
    selected = out / 'SELECTED-PROFILES.md'
    sections = []
    for profile in profiles:
        profile_text = (out / 'profiles' / profile / 'PROFILE.md').read_text(encoding='utf-8')
        sections.append(f'## {profile}\n\n{profile_text}')
    selected.write_text(
        '# پروفایل‌های انتخاب‌شده\n\n'
        f'- حالت اجرا: `{args.risk}`\n\n'
        + '\n\n---\n\n'.join(sections),
        encoding='utf-8',
    )

    print(f'Created MASEF project at: {out}')
    print(f"Profiles: {', '.join(profiles)}")
    print(f'Execution mode: {args.risk}')
    print('Next: run python scripts/validate_framework.py and let Codex execute START-HERE.md')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
