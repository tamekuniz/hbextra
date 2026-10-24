import importlib
import os
import shutil
import sys
import tempfile
import unittest

# Test-only credentials.
TEST_PASSWORD = 'pass1234'  # nosec B105


class HBExtraTagFoldTest(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix='hbextra-test-')
        os.environ['HBEXTRA_DATA_DIR'] = self.tmpdir
        sys.modules.pop('hbextra', None)
        self.hbextra = importlib.import_module('hbextra')
        self.hbextra.init_db()
        self.client = self.hbextra.app.test_client()
        self.client.post('/hbextra/api/register', json={'username': 'alice', 'password': TEST_PASSWORD})
        csrf = self.client.get('/hbextra/api/me').json['csrf_token']
        entries = [
            ('https://example.com/a', '2026-06-01T00:00:00+00:00', [{'tag': 'Linux', 'count': 3}, {'tag': 'rare', 'count': 1}]),
            ('https://example.com/b', '2026-06-05T00:00:00+00:00', [{'tag': 'linux', 'count': 1}, {'tag': 'Rare', 'count': 1}]),
        ]
        payload = {
            'entries': [{'url': u, 'title': 't', 'date': d, 'count': 1, 'cats': [], 'tags': tags, 'tags_loaded': 1}
                        for u, d, tags in entries],
            'memberships': [{'url': u, 'mode': 'new', 'cat': ''} for u, _, _ in entries],
        }
        res = self.client.post('/hbextra/api/import', json=payload, headers={'X-CSRF-Token': csrf})
        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        sys.modules.pop('hbextra', None)
        os.environ.pop('HBEXTRA_DATA_DIR', None)
        shutil.rmtree(self.tmpdir)

    def tags(self, url):
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.json
        return {t['tag']: t for t in data.get('tags', data.get('top_tags_all'))}

    def test_default_keeps_case_variants_separate(self):
        for url in ('/hbextra/api/tags?mode=new&cat=', '/hbextra/api/entries?mode=new&cat='):
            with self.subTest(url=url):
                self.assertEqual({k: v['count'] for k, v in self.tags(url).items()}, {'Linux': 3})

    def test_fold_merges_case_variants(self):
        for url in ('/hbextra/api/tags?mode=new&cat=&fold=1', '/hbextra/api/entries?mode=new&cat=&fold=1'):
            with self.subTest(url=url):
                tags = self.tags(url)
                self.assertEqual(set(tags), {'Linux', 'rare'})
                self.assertEqual(tags['Linux']['count'], 4)
                self.assertEqual(tags['Linux']['last'], '2026-06-05T00:00:00+00:00')
                self.assertEqual(tags['rare']['count'], 2)


if __name__ == '__main__':
    unittest.main()
