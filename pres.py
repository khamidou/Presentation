#!/usr/bin/env python
# The python script that generates the needed html code for a keynote.

import sys
import os
from shutil import copytree, rmtree
from textile import textile
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('templates'))

def templ(name, **args):
	return env.get_template(name).render(**args)

slides = []

for file in sorted(os.listdir('./presentation/')):
    slides.append(textile(open('./presentation/' + file).read()))

rmtree("./output")
os.mkdir("./output")
open("./output/index.htm", "w+").write(templ("index.htm", slides=slides, num_slides=len(slides)))
copytree("js", "output/js")
copytree("static", "output/static")

print "The presentation has been generated."
