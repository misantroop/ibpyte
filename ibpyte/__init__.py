#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# Sugary sweet layer of icing on top of the TWS API.
#
# Use:
#    {{{
#    from ibpyte import ibConnection, message
#
#    def my_callback(msg):
#        ...
#
#    con = ibConnection()
#    con.register(my_callback, message.TickSize, message.TickPrice)
#    con.connect()
#    con.reqAccountUpdates(...)
#    ...
#    con.unregister(my_callback, message.TickSize)
#    }}}
#
from ibpyte.connection import Connection


##
# This is the preferred client interface to this module.
# Alternatively, the Connection type can be sub-classed an its
# 'create' classmethod reused.
ibConnection = Connection.create
