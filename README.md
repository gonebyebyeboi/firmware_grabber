# EMBA Tool Firmware Name Grabber
This project is a Python script that looks through completed EMBA firmware scans, and searches for the names of the firmware. This tool was built because some of the names of the firmware didn't show up in the completed scans that were ran. It returns a dictionary that details the name of the firmware, along with the Hex GUID, so that specific results for firmware can be found in the base directory.

## Goals for this script
The goal of this script was to streamline the exploratory analysis of our EMBA scans, which there are close to 1600 scan reports, so that a research paper could be completed on Agentic LLM Analysis of cybersecurity data.

Dependencies do exist for this script, so be sure to run:
```
pip install -r requirements.txt
```

**NOTE:** I built this script to aid in our research of agentic workflows, and is incomplete due to unforeseen obstacles in our research environment.


