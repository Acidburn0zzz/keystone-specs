# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import glob

import docutils.core
import testtools
from testtools import matchers


TITLES = {
    'Problem Description': [],
    'Proposed Change': [
        'Alternatives',
        'Data Model Impact',
        'REST API Impact',
        'Security Impact',
        'Notifications Impact',
        'Other End User Impact',
        'Performance Impact',
        'Other Deployer Impact',
        'Developer Impact',
    ],
    'Implementation': [
        'Assignee(s)',
        'Work Items',
    ],
    'Dependencies': [],
    'Testing': [],
    'Documentation Impact': [],
    'References': [],
}


class TestTitles(testtools.TestCase):
    def _get_title(self, section_tree):
        section = {
            'subtitles': [],
        }
        for node in section_tree:
            if node.tagname == 'title':
                section['name'] = node.rawsource
            elif node.tagname == 'section':
                # Note subsection subtitles are thrown away
                subsection = self._get_title(node)
                section['subtitles'].append(subsection['name'])
        return section

    def _get_titles(self, spec):
        titles = {}
        for node in spec:
            if node.tagname == 'section':
                section = self._get_title(node)
                titles[section['name']] = section['subtitles']
        return titles

    def _check_titles(self, titles):
        self.assertEqual(TITLES, titles)

    def test_template(self):
        files = ['specs/template.rst'] + glob.glob('specs/*/*')
        for filename in files:
            self.assertThat(filename, matchers.EndsWith('.rst'),
                            'spec\'s file must use the "rst" extension.')
            with open(filename) as f:
                data = f.read()
            spec = docutils.core.publish_doctree(data)
            titles = self._get_titles(spec)
            self._check_titles(titles)