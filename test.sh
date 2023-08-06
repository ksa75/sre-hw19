#!/bin/bash
curl -v http://192.168.19.128:81 2>/dev/null| grep example | wc -l