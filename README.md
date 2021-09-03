## Overview
Simple script with hardcoded paths to ingest a JSONLINES file and output a csv file. If ingesting a dynamo DB json export, you will need to do some pre-processing manually to get it to a json lines format. Namely removing braces, data identifies like "S" and "N" etc. 
