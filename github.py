#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Ravi Sharma <me@rvish.com>

# Copyright (c) 2015 Ravi Sharma (http://www.rvish.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import subprocess
import sys

class Git(object):

    def __init__(self, username):
        self.username = username
        self.API_URL = "https://api.github.com/users/"

    @staticmethod
    def sanitizeResults(string):
        return string.replace(',','').replace('"','')

    def getEmails(self):
        # Preparing command
        cmd = "curl " + self.API_URL+self.username+" | grep email | cut -d: -f2"

        # Running Command
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

        # Parse email
        result = self.sanitizeResults(process.communicate()[0])

        if "null" not in result:
            return result
        else:
            # Preparing command
            cmd = "curl " + self.API_URL+self.username+"/events/public | grep email | sort -u | cut -d: -f2"

            # Running Command
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

            # Parse Email
            return self.sanitizeResults(process.communicate()[0])

    def getFollowers(self):
        # Preparing command
        cmd = "curl " + self.API_URL + self.username+"/followers | grep login | sort -u | cut -d: -f2"

        # Running Command
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

        # Parse Email
        return self.sanitizeResults(process.communicate()[0])

    def getFollowing(self):
        # Preparing command
        cmd = "curl " + self.API_URL + self.username+"/following | grep login | sort -u | cut -d: -f2"

        # Running Command
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

        # Parse Email
        return self.sanitizeResults(process.communicate()[0])


def main(email):
    g = Git(email)
    print(g.getEmails())

if __name__ == '__main__':
    main(*sys.argv[1:])  # skipping the first entry as its the name of this file