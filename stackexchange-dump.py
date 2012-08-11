# Copyright (c) Alex Chamberlain 2012
# Licensed under MIT license

import sys
import os
from pprint import pprint
from stackpy import Site
from optparse import OptionParser
from pystache import render

if __name__ == "__main__":
  parser = OptionParser()
  parser.add_option("-f", "--format", type="string", dest="format", default="html", help="Output format")
  parser.add_option("-t", "--template_dir", type="string", dest="template_dir", default="./template", help="Template Directory")
  (options, args) = parser.parse_args()

  site = Site('stackoverflow')
  #site.be_inclusive()

  if len(args) == 0:
    id = int(raw_input("Enter a question ID: "))
  else:
    id = int(args[0])

  question = site.questions(id).filter('withbody')[0]
  owner    = site.users(question.owner.user_id)[0]
  answer   = site.answers(question.accepted_answer_id).filter('withbody')[0]
  answerer = site.users(answer.owner.user_id)[0]

  data = {
    'question': {
      'title': question.title,
      'link': question.link,
      'body': question.body,
      'owner': {
        'link': owner.link,
        'display_name': owner.display_name
      }
    },
    'answer': {
      'body': answer.body,
      'owner': {
        'link': answerer.link,
	'display_name': answerer.display_name
      }
    }
  }

  options.template     = ''.join([options.template_dir, '/', options.format])

  if os.path.isfile(options.template):
    t = open(options.template).read()
    print render(t, data).encode('utf-8')
  else:
    print 'Invalid format option'
