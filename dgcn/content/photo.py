from five import grok
from plone.directives import form
from plone.dexterity.content import Item

from zope import schema
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage

from dgcn.content import MessageFactory as _


class IPhoto(form.Schema):
    """Photo Interface Class to Define Content-Type Schema
    """

    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/photo.xml to define the content type
    # and add directives here as necessary.

    #form.model("models/photo.xml")

    id = schema.TextLine(
        title=_(u"Image ID"),
    )

    id_vcea = schema.TextLine(
        title=_(u"ID at vcea.net"),
        required=False,
    )

    id_ref = schema.TextLine(
        title=_(u"HPC Reference"),
        required=False,
    )

    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )

    title_alt = schema.TextLine(
        title=_(u"Alternative Title"),
        required=False,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    form.primary('image')
    image = NamedBlobImage(
        title=_(u"Photo"),
        required=False,
    )

    collection = schema.TextLine(
        title=_(u"Collection"),
        required=False,
    )

    coverage = schema.TextLine(
        title=_(u"Coverage"),
        required=False,
    )

    year = schema.TextLine(
        title=_(u"Year"),
        required=False,
    )

    date = schema.TextLine(
        title=_(u"Date"),
        required=False,
    )

    estimated = schema.TextLine(
        title=_(u"Estimated Date"),
        required=False,
    )

    photographer = schema.TextLine(
        title=_(u"Photographer"),
        required=False,
    )

    caption = schema.TextLine(
        title=_(u"Caption"),
        required=False,
    )

    cap_abm = schema.TextLine(
        title=_(u"Caption in Album or on Mount"),
        required=False,
    )

    cap_img = schema.TextLine(
        title=_(u"Caption on Original Image"),
        required=False,
    )

    frmt_orig = schema.TextLine(
        title=_(u"Original Format"),
        required=False,
    )

    material = schema.TextLine(
        title=_(u"Material Form of Image"),
        required=False,
    )

    note = schema.Text(
        title=_(u"Note"),
        required=False,
    )

    url = schema.TextLine(
        title=_(u"URL"),
        required=False,
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Photo(Item):
    grok.implements(IPhoto)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# photo_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    grok.context(IPhoto)
    grok.require('zope2.View')
    grok.name('view')

