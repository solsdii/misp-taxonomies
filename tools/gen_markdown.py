#!/usr/bin/env python3

import json
from pathlib import Path
from datetime import datetime

TAXONOMY_ROOT_PATH = Path(__file__).resolve().parent.parent


def fetchTaxonomies():
    taxonomiesFolder = TAXONOMY_ROOT_PATH
    taxonomies = []
    for taxonomyFile in taxonomiesFolder.glob('./*/machinetag.json'):
        with open(taxonomyFile) as f:
            taxonomy = json.load(f)
            taxonomies.append(taxonomy)
    return taxonomies

def generateMarkdown(taxonomies):
    markdown_line_array = []
    markdown_line_array.append("# Taxonomies")
    markdown_line_array.append("- Generation date: %s" % datetime.now().isoformat().split('T')[0])
    markdown_line_array.append("- license: %s" % 'CC-0')
    markdown_line_array.append("- description: %s" % 'Manifest file of MISP taxonomies available.')
    markdown_line_array.append("")
    
    markdown_line_array.append("## Taxonomies")
    markdown_line_array.append("")
    for taxonomy in taxonomies:
        markdown_line_array.append("### %s" % taxonomy['namespace'])
        markdown_line_array.append("- description: %s" % taxonomy['description'])
        markdown_line_array.append("- version: %s" % taxonomy['version'])
        markdown_line_array.append("- Predicates")
        markdown_line_array = markdown_line_array + ['    - '+p['value'] for p in taxonomy['predicates']]
    markdown = '\n'.join(markdown_line_array)
    return markdown

def saveMarkdown(markdown):
    with open(TAXONOMY_ROOT_PATH / 'Summary.md', 'w') as f:
        f.write(markdown)

def awesomePrint(text):
    print('\033[1;32m{}\033[0;39m'.format(text))

if __name__ == "__main__":
    taxonomies = fetchTaxonomies()
    markdown = generateMarkdown(taxonomies)
    saveMarkdown(markdown)
    awesomePrint('> Markdown saved!')