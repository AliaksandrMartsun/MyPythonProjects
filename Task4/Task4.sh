#!/bin/bash
touch file_{1..3}.txt 
touch file_{4..5}.notxt 
rm *notxt
