#!/usr/bin/env python3

import click

click.clear()

mod_value = 37

with open('message.txt') as message:
    for line in message:
        data = line.split()
        for i in data:
            new_data = int(i) % mod_value
            print(new_data)