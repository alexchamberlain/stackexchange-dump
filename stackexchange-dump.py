# Copyright (c) Alex Chamberlain 2012
# Licensed under MIT license

import sys
from stackpy import Site

site = Site('stackoverflow')
#site.be_inclusive()

if len(sys.argv) < 2:
  id = int(raw_input("Enter a question ID: "))
else:
  id = int(sys.argv[1])

question = site.questions(id).filter('withbody')[0]
owner    = site.users(question.owner.user_id)[0]
answer   = site.answers(question.accepted_answer_id).filter('withbody')[0]
answerer = site.users(answer.owner.user_id)[0]

print '<h1>%s</h1>' % question.title
print '<p><a href="%s">%s</a><br />' % (question.link, question.link)
print 'Asked by <a href="%s">%s</a> on StackOverflow.com</p>' % (owner.link, owner.display_name)
print question.body
print '<h2>Accepted Answer</h2>'
print 'Answered by <a href="%s">%s</a>' % (answerer.link, answerer.display_name)
print answer.body
print '<p>Reproduced under the Creative Commons Attribution-ShareAlike 3.0 Unported license.</p>'
