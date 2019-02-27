#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None, **attributes):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = attributes

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write('<{}>\n'.format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write('\n')
        out_file.write('</{}>\n'.format(self.tag))


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'

    def render(self, out_file):
        # out_file.write('<{}'.format(self.tag))
        # for content in self.contents:
        #     try:
        #         content.render(out_file)
        #     except AttributeError:
        #         out_file.write(content)
        #     out_file.write('\n')
        # out_file.write('</{}>\n'.format(self.tag))
        #
        open_tag = ['<{} '.format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append('{}="{}" '.format(key, value))
        open_tag.append('>\n')
        out_file.write(''.join(open_tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write('\n')
        out_file.write('</{}>\n'.format(self.tag))


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    tag = 'one line tag'

    def render(self, out_file):
        out_file.write('<{}>'.format(self.tag))
        out_file.write(self.contents[0])
        out_file.write('</{}>\n'.format(self.tag))

    def append(self, new_content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    pass


class Hr(SelfClosingTag):
    tag = "hr"
