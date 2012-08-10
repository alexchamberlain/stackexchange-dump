import sys
import stackexchange

site = stackexchange.Site(stackexchange.StackOverflow)
site.be_inclusive()

if len(sys.argv) < 2:
  id = int(raw_input("Enter a question ID: "))
else:
  id = int(sys.argv[1])

question = site.question(id)
owner    = site.user(question.owner.id)
answer   = site.answer(question.accepted_answer_id)
answerer = site.user(answer.owner_id)

print '<h1>%s</h1>' % question.title
print '<a href="%s">%s</a>' % (question.url, question.url)
print 'Asked by <a href="%s">%s</a>' % (owner.url, owner.display_name)
print question.body
print '<h2>Accepted Answer</h2>'
print 'Answered by <a href="%s">%s</a>' % (answerer.url, answerer.display_name)
print answer.body
