from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.dom import DOM


class TestDOM(unittest.TestCase):
    def test_create_element(self):
        self.assertEqual(DOM.create_element('p', {'className': 'intro'}, 'Test test').tag, 'p')
        self.assertEqual(DOM.create_element('p', {'className': 'intro'}, 'Test test').get('class'), 'intro')
        self.assertEqual(DOM.create_element('p', {'className': 'intro'}, 'Test test').text, 'Test test')

    def test_create_element_empty(self):
        self.assertEqual(DOM.create_element().tag, 'fragment')

    def test_create_element_nested(self):
        self.assertEqual(DOM.render(DOM.create_element('a', {}, DOM.create_element('span', {'className': 'file-info icon-text'}, DOM.create_element('span', {'className': 'icon-text__text'}, 'Test test'), DOM.create_element('svg', {'className': 'icon'}, DOM.create_element('use', {'xlink:href': 'icon-test'}))))), '<a><span class="file-info icon-text"><span class="icon-text__text">Test test</span><svg class="icon"><use xmlns:ns0="http://www.w3.org/1999/xlink" ns0:href="icon-test"></use></svg></span></a>')

    def test_create_document_fragment(self):
        self.assertEqual(DOM.create_document_fragment().tag, 'fragment')

    def test_create_text_node(self):
        self.assertEqual(DOM.create_text_node('Test text').tag, 'textnode')
        self.assertEqual(DOM.create_text_node('Test text').text, 'Test text')

    def test_parse_html(self):
        self.assertEqual(DOM.render(DOM.parse_html('<p><span>Test text</span></p>')), '<p><span>Test text</span></p>')

    def test_append_child(self):
        parent = DOM.create_element('p')
        DOM.append_child(parent, DOM.create_element('span', {}, 'Test text'))
        self.assertEqual(DOM.render(parent), '<p><span>Test text</span></p>')

    def test_set_attribute(self):
        elt = DOM.create_element('a')
        DOM.set_attribute(elt, 'href', 'http://example.com')
        self.assertEqual(elt.get('href'), 'http://example.com')

    def test_set_text_content(self):
        elt = DOM.create_element('p')
        DOM.set_text_content(elt, 'Test test')
        self.assertEqual(elt.text, 'Test test')

    def test_get_children(self):
        self.assertEqual(len(DOM.get_children(DOM.create_element('span', {}, DOM.create_element('span'), DOM.create_element('span')))), 2)

    def test_render(self):
        self.assertEqual(DOM.render(DOM.create_element('a', {}, DOM.create_element('span', {'className': 'file-info icon-text'}, DOM.create_element('span', {'className': 'icon-text__text'}, 'Test test'), DOM.create_element('svg', {'className': 'icon'}, DOM.create_element('use', {'xlink:href': 'icon-test'}))))), '<a><span class="file-info icon-text"><span class="icon-text__text">Test test</span><svg class="icon"><use xmlns:ns0="http://www.w3.org/1999/xlink" ns0:href="icon-test"></use></svg></span></a>')

    def test_pretty_print(self):
        self.assertEqual(DOM.pretty_print('<a><span class="file-info icon-text"><span class="icon-text__text">Test test</span><svg class="icon"><use xmlns:ns0="http://www.w3.org/1999/xlink" ns0:href="icon-test"></use></svg></span></a>'), '\n  <a>\n    <span class="file-info icon-text">\n      <span class="icon-text__text">Test test</span>\n      <svg class="icon">\n        <use xmlns:ns0="http://www.w3.org/1999/xlink" ns0:href="icon-test"/>\n      </svg>\n    </span>\n  </a>\n\n')