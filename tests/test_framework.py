import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class FrameworkTests(unittest.TestCase):
    def test_agents_has_required_sections(self):
        text = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        self.assertIn('## قواعد اجرای کار', text)
        self.assertIn('## پایان کار', text)

    def test_profiles_exist(self):
        for profile in ['generic', 'wordpress-plugin', 'webapp', 'api-service', 'religious-product']:
            self.assertTrue((ROOT / 'profiles' / profile / 'PROFILE.md').is_file(), profile)

    def test_skills_have_frontmatter(self):
        skills = list((ROOT / '.agents/skills').glob('*/SKILL.md'))
        self.assertGreaterEqual(len(skills), 4)
        for skill in skills:
            text = skill.read_text(encoding='utf-8')
            self.assertTrue(text.startswith('---\n'), str(skill))
            self.assertIn('\nname:', text)
            self.assertIn('\ndescription:', text)

    def test_bootstrap_script_supports_combined_profiles(self):
        text = (ROOT / 'scripts/bootstrap_project.py').read_text(encoding='utf-8')
        self.assertIn("action='append'", text)
        self.assertIn('SELECTED-PROFILES.md', text)


if __name__ == '__main__':
    unittest.main()
