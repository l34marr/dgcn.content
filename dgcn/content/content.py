from zope.interface import implements
from plone.dexterity.content import Item

from dgcn.content.interfaces import IPhoto


class Photo(Item):
    implements(IPhoto)

