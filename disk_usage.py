#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:28:32 2020

@author: tstan
"""

import re
log = "July 21 07:51:48 mycomputer bad_proces[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
