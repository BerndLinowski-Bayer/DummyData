
Systag DB Access
================

This is a *tiny bit* of RST documentation.

It is planned to provide the following functionality:

* Connecting to a MS SQL server with support for

  * Reading connection settings from a file (JSON)
  * Reading connection settings from environment parameters
  * or a combination of both (allows to store DB server-name, DB-name, schema, user-name etc. in a file but provide the password in an enviroment variable)
  * Connection retries
  * R-connect "on the fly"

* Reading query results in Pandas Data-Frames

