import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class FrameworkTests(unittest.TestCase):
    def test_agents_has_required_sections(self):
        text = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        self.assertIn('## اصل استقلال فنی', text)
        self.assertIn('## موارد نیازمند توقف انسانی', text)
        self.assertIn('## پایان کار', text)

    def test_technical_profiles_exist(self):
        for profile in ['generic', 'wordpress-plugin', 'webapp', 'api-service']:
            self.assertTrue((ROOT / 'profiles' / profile / 'PROFILE.md').is_file(), profile)
        self.assertFalse((ROOT / 'profiles/religious-product/PROFILE.md').exists())

    def test_skills_have_frontmatter(self):
        skills = list((ROOT / '.agents/skills').glob('*/SKILL.md'))
        self.assertGreaterEqual(len(skills), 3)
        self.assertFalse((ROOT / '.agents/skills/religious-integrity/SKILL.md').exists())
        for skill in skills:
            text = skill.read_text(encoding='utf-8')
            self.assertTrue(text.startswith('---\n'), str(skill))
            self.assertIn('\nname:', text)
            self.assertIn('\ndescription:', text)

    def test_bootstrap_supports_profiles_and_risk_modes(self):
        text = (ROOT / 'scripts/bootstrap_project.py').read_text(encoding='utf-8')
        self.assertIn("action='append'", text)
        self.assertIn("choices=['light', 'standard', 'critical']", text)
        self.assertIn('SELECTED-PROFILES.md', text)
        self.assertNotIn("'religious-product'", text)

    def test_religious_workflow_is_removed(self):
        self.assertFalse((ROOT / 'docs/02-domain/RELIGIOUS-INTEGRITY.md').exists())
        paths = [
            ROOT / 'README.md',
            ROOT / 'START-HERE.md',
            ROOT / 'AGENTS.md',
            ROOT / 'docs/00-governance/RISK-PROFILE.md',
            ROOT / 'docs/01-product/REQUIREMENTS.md',
            ROOT / 'docs/01-product/ACCEPTANCE-CRITERIA.md',
            ROOT / 'docs/06-quality/TEST-STRATEGY.md',
            ROOT / '.github/PULL_REQUEST_TEMPLATE.md',
        ]
        forbidden = [
            'religious-product',
            'Religious Review',
            'Religious Integrity Gate',
            'محتوای دینی حساس',
        ]
        for path in paths:
            text = path.read_text(encoding='utf-8')
            for marker in forbidden:
                self.assertNotIn(marker, text, f'{path}: {marker}')


if __name__ == '__main__':
    unittest.main()
