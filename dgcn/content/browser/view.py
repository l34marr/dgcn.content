from Products.Five.browser import BrowserView
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


class MyView(BrowserView):

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None

