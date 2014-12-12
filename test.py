#! /usr/bin/python3

import sys
import os
import langid
import collections

def test_one(ident, cm, xfail_languages, fname):
    lang = os.path.basename(fname)
    lang = lang[:lang.find('.')]
    if lang[-1] == '_':
        lang = lang[:-1]
        xfail_languages.add(lang)

    with open(fname) as f:
        text = "\n".join(ll for ll in (l.strip() for l in f)
                         if ll and ll[0] != '#')

    result = ident.classify(text)[0]
    cm[lang][result] += 1

def main():
    ident = langid.LanguageIdentifier.from_model(norm_probs=False)
    cm = collections.defaultdict(collections.Counter)

    xfail_languages = set()
    for fname in os.listdir("tests"):
        if fname.endswith(".txt"):
            test_one(ident, cm, xfail_languages, "tests/" + fname)

    all_languages = set()
    for row, col in cm.items():
        all_languages.add(row)
        all_languages.update(col.keys())

    misid_from = set()
    misid_to   = set()
    for row in all_languages:
        for col in all_languages:
            if row != col:
                if cm[row][col]:
                    misid_from.add(row)
                    misid_to.add(col)

    misid_from = sorted(misid_from)
    misid_to   = sorted(misid_to)

    sys.stdout.write("<!doctype html>\n<meta charset=\"utf-8\">\n"
                     "<style>\n"
                     " .x  { background: #ddd }\n"
                     " .y  { background: #4d4 }\n"
                     " .n  { background: #d44 }\n"
                     " .yx { background: #8d8 }\n"
                     " .nx { background: #d88 }\n"
                     "</style>\n"
                     "<table><tr><th></th>\n")
    for lang in misid_to:
        cl = (' class="x"' if lang in xfail_languages else '')
        sys.stdout.write("<th{}>{}</th>".format(cl, lang))
    sys.stdout.write("</tr>\n")
    for row in misid_from:
        cl = (' class="x"' if row in xfail_languages else '')
        sys.stdout.write("<tr><th{}>{}</th>".format(cl, row))
        for col in misid_to:
            n = cm[row][col]
            cl = ""
            if n > 0:
                if row == col:
                    cl = "y"
                else:
                    cl = "n"
            if row in xfail_languages or col in xfail_languages:
                cl += "x"
            if cl:
                cl = ' class="{}"'.format(cl)
            if n > 1:
                sys.stdout.write("<td{}>{}</td>".format(cl, n))
            else:
                sys.stdout.write("<td{}></td>".format(cl))
        sys.stdout.write("</tr>\n")
    sys.stdout.write("</table>\n")

main()
