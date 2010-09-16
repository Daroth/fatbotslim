# -*- coding: utf-8 -*-
#
#   Copyright (c) 2010 MatToufoutu
#
#   This file is part of fatbotslim.
#   fatbotslim is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   fatbotslim is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with fatbotslim.  If not, see <http://www.gnu.org/licenses/>.
#

from plugins import BasePlugin, trigger
from include.whois import whois, WhoisError, SUFFIXES
from include.utils import formatted

class Whois(BasePlugin):
    name = "Whois"
    description = "Display the whois record for a given domain"
    pubHelp = """
    !whois <domain> - get the whois record for a domain
    """

    def getWhois(self, user, destination, message):
        domain = message.split('.')[-1]
        if domain not in SUFFIXES:
            result = formatted("Domain is not valid: %s" % domain, 'red')
            self.client.msg(destination, result)
            return
        try:
            result = whois(message)
            result = "Domain '%s' is already registered :(\nExpiration date: %s" % (message, result.expiration_date)
            result = formatted(result, 'red')
            result = formatted(result, 'bold')
        except WhoisError:
            result = "No result for '%s'" % message
            result = formatted(result, 'green')
            result = formatted(result, 'bold')
        self.client.msg(destination, result)

    @trigger('!whois', getWhois)
    def on_pubmsg(self, user, destination, message):
        pass
