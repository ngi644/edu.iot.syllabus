# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from edu.iot.syllabus import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.autoform import directives
from plone.supermodel.directives import fieldset
from plone.supermodel.directives import primary
from plone.supermodel import model


class IEduIotSyllabusLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IUnit(model.Schema):
    """
    Unit type
    """

    experimental_list = schema.List(
        title=_(u'Experimental Titles'),
        required=False,
        value_type=schema.TextLine(title=_(u'Experimental'),)
    )

    group_count = schema.Int(
        title=_(u'Group count'),
        required=False,
    )


class ISubject(model.Schema):
    """
    Unit type
    """

    year = schema.Int(
        title=_(u'Year'),
        required=False,
    )
