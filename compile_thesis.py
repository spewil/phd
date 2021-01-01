#!/usr/bin/env python

# to compile from command line:
# mdmerge -o thesis.md outline.md; p3 compile_thesis.py
# first command transcludes sections into main markdown file
# second command converts thesis.md to thesis.html with all the bells
# pandoc templates
# https://pandoc.org/MANUAL.html#templates
# default templates

import pypandoc
import jinja2
from pathlib import Path
import markdown

file_loader = jinja2.FileSystemLoader('.')
env = jinja2.Environment(loader=file_loader)
template = env.get_template('base.html')


def main():
    pdoc_args = [
        '--toc',
        '--toc-depth=4',
        '-s',  # standalone?
        '--bibliography=bibliography.bib',
        '--metadata',
        'link-citations=true',  # make citation links
        '--csl=nature.csl',
        '--mathml',  # this works in chrome and firefox
        "--css=pandoc.css",  # custom css
        "--include-in-header",  # custom header -- so I can add hypothesis, etc
        "header.html",
        "--template",
        "template.html"
    ]
    filters = ['pandoc-citeproc']
    input_path = Path("thesis.md")
    output_path = input_path.parent / Path("index.html")
    # processFile(input_path, "thesis_toc.md")
    html = pypandoc.convert_file(input_path.name,
                                 'html5',
                                 format='md',
                                 extra_args=pdoc_args,
                                 filters=filters)
    doc = template.render(content=html)
    with open(output_path, 'w') as outfile:
        outfile.write(doc)


def processFile(inFile, outFile):
    mdFile = open(inFile, 'r')
    toc = []
    levels = [0, 0, 0, 0]
    newFile = open(outFile, 'w')
    tempFile = []
    tocLoc = 0
    partOfToc = False

    for line in mdFile:
        if partOfToc and line != '\n':
            continue
        else:
            partOfToc = False
        if 'Table of Contents' in line:
            tocLoc = len(tempFile) + 1
            partOfToc = True
        elif line[0] == '#':
            secId = buildToc(line, toc, levels)
            line = addSectionTag(cleanLine(line), secId) + '\n'
        tempFile.append(line)

    for line in toc:
        tempFile.insert(tocLoc, line)
        tocLoc += 1

    for line in tempFile:
        newFile.write(line)

    mdFile.close()
    newFile.close()


def addSectionTag(line, secId):
    startIndex = line.find(' ')
    line = line[:startIndex +
                1] + '<a id=\'' + secId + '\' />' + line[startIndex + 1:]
    return line


def buildToc(line, toc, levels):
    line = cleanLine(line)
    vspace = "   "
    if line[:4] == '####':
        link = line[5:].strip().lower().replace(" ", "-")
        toc.append(vspace * 3 + '* [' + line[5:] + '](#' + link + ')\n')
    elif line[:3] == '###':
        link = line[4:].strip().lower().replace(" ", "-")
        toc.append(vspace * 2 + '* [' + line[4:] + '](#' + link + ')\n')
    elif line[:2] == '##':
        link = line[3:].strip().lower().replace(" ", "-")
        toc.append(vspace * 1 + '* [' + line[3:] + '](#' + link + ')\n')
    elif line[:1] == '#':
        link = line[2:].strip().lower().replace(" ", "-")
        toc.append('* [' + line[2:] + '](#' + link + ')\n')
    return link


def cleanLine(text):
    text = stripNewline(text)
    text = removeAnchors(text)
    return text


def stripNewline(text):
    return text.replace('\n', '')


def removeAnchors(text):
    while ('<' in text and '>' in text):
        leftTag = text.index('<')
        rightTag = text.index('>')
        text = text[0:leftTag] + text[rightTag + 1:]
    return text


if __name__ == '__main__':
    main()
