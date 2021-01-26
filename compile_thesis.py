#!/usr/bin/env python

# pandoc templates
# https://pandoc.org/MANUAL.html#templates

# using two filters from pypi:
# https://github.com/tomduck/pandoc-xnos
# pandoc-include to transclude markdown files

import pypandoc
import jinja2
from pathlib import Path
import click

file_loader = jinja2.FileSystemLoader('.')
env = jinja2.Environment(loader=file_loader)
template = env.get_template('base.html')


def main():
    pdoc_args = [
        '--toc',
        '--toc-depth=4',
        '--number-sections',
        '--filter',
        'pandoc-include',
        '--filter',
        'pandoc-xnos',
        '--bibliography=bibliography.bib',
        '--metadata',
        'link-citations=true',  # make citation links
        '--csl=nature.csl',
        '--mathml',  # this works in chrome and firefox
        "--css=pandoc.css",  # custom css
        # "--include-before-body",
        # "preamble.tex",
        "--include-in-header",  # custom header -- so I can add hypothesis, etc
        "header.html",
        "--template",
        "template.html",
        "--citeproc"
    ]

    input_path = Path("thesis.md")
    output_path = input_path.parent / Path("index.html")
    tex_path = Path("thesis.tex")
    html = pypandoc.convert_file(input_path.name,
                                 'html5',
                                 outputfile="index.html",
                                 format='md',
                                 extra_args=pdoc_args)

    doc = template.render(content=html)
    with open(output_path, 'w') as outfile:
        outfile.write(doc)

    # save tex file
    pypandoc.convert_file(input_path.name,
                          'latex',
                          format='md',
                          extra_args=pdoc_args,
                          outputfile=tex_path.name)


@click.command()
@click.argument('input_file', type=str)
@click.argument('output_type', default='html', type=str)
def compile_to_pdf(input_file, output_type):
    pdoc_args = [
        '--number-sections',
        '--filter',
        'pandoc-include',
        '--filter',
        'pandoc-xnos',
        '--bibliography=bibliography.bib',
        '--metadata',
        'link-citations=true',  # make citation links
        '--csl=nature.csl',
        # "--include-before-body",
        # "preamble.tex",
        # '--template',
        # "template.tex",
        "--citeproc"
    ]
    # output_path = input_path.parent / Path("index.html")
    pypandoc.convert_file(source_file=input_file,
                          format='md',
                          to='pdf',
                          outputfile="thesis.pdf",
                          extra_args=pdoc_args)


if __name__ == '__main__':
    import sys
    try:
        sys.argv[1]
        compile_to_pdf()
    except IndexError:
        main()