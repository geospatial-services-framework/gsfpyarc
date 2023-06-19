# Change Log
All notable changes to this project will be documented in this file.

# 2.0.0 / 2023-04-17
- The main reason for this breaking change is the switch from the ese request handler to the gsf request handler. The ese request handler is no longer supported by default in gsf 2.x.  Though this python interface to gsf has not changed much gsfpy 2.0 will no longer support gsf 1.x by default.
- This package no longer supports Python 2.

# 2.0.1 / 2023-06-16
- The job progress and messages are displayed in ArcGIS Pro.
- Cancelling a job in ArcGIS Pro actually sends a cancel request to GSF.