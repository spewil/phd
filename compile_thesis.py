#!/usr/bin/env python

# pandoc templates
# https://pandoc.org/MANUAL.html#templates

# using two filters from pypi:
# https://github.com/tomduck/pandoc-xnos
# pandoc-include to transclude markdown files

import pypandoc
import click
import os


def main():
    os.chdir("build/html")

    pdoc_args = [
        '--toc',
        '--toc-depth=4',
        '--number-sections',
        '--filter',
        'pandoc-include',
        '--filter',
        'pandoc-xnos',
        '--bibliography=../assets/bibliography.bib',
        '--metadata',
        'link-citations=true',  # make citation links
        '--csl=../assets/nature.csl',
        '--mathml',  # this works in chrome and firefox
        "--css=../../pandoc.css",  # custom css
        # "--include-before-body",
        # "preamble.tex",
        "--include-in-header",  # custom header -- so I can add hypothesis, etc
        "header.html",
        "--template",
        "template.html",
        "--citeproc"
    ]

    input_path = "thesis.md"
    pypandoc.convert_file(input_path,
                          'html5',
                          outputfile="../../index.html",
                          format='md',
                          extra_args=pdoc_args)


@click.command()
@click.argument('input_file', type=str)
@click.argument('output_type', default='html', type=str)
def compile_to_pdf(input_file, output_type):
    os.chdir("build/latex")
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
        # "template",
        "--citeproc",
        "--verbose"
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
        print(f"compiling {sys.argv[1]}")
        compile_to_pdf()
    except IndexError:
        print("compiling to index.html")
        main()