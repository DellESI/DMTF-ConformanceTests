# DMTF-ConformanceTests
Latest Known Validated Set of Conformance Tests
```
The DellESI redfish service in rackmanager-tools should
be "conformant" with the redfish standard.
This series of tests, if passing, should establish conformity.

git clone https://github.com/DellESI/DMTF-ConformanceTests
  These are what we consider the "stable" versions.
  These are what Test should use.

DMTF is constantly updating and improving but their latest
should be tested before adding to the stable repository.

1)Every command has a suggested place to save stdout.
  You probably want to customize.
2)Most commands specify the DUT as localhost.
  You probably  want to change that.
3)All the commands have -h option for full set of options.
  In the samples below are the options that I use.

---------------------------
Mockup Creators creates a directory of redfish APIs,
  the json resources and the response headers
Be aware of the -D option. You will use the mockup later.
Use the -H, headers may be useful later.

cd ~/DMTF-ConformanceTests/Redfish-Mockup-Creator
rm -rf ~/yourmockupname
python3 redfishMockupCreate.py -T -H -r localhost -u root -p calvin -S -D ~/yourmockupname 2>&1|tee  yourlogname
NOTE: This puts the mockup in the home directory.

---------------------------
The JSON schemas at http://redfish.dmtf.org/schemas/v1/ define the
properties of every redfish resource. The urls are pointed to by
the odata.type and/or a Link in the header.
The simplest is to use the -S option which will fetch the online
schemas. But you can also get the schemas locally with my getSchemas.py.

cd ~/DMTF-ConformanceTests/Redfish-JsonSchema-ResponseValidator
python3 Redfish-JsonSchema-ResponseValidator.py -S -m ~/yourmockupname 2>&1|tee  yourlogname

---------------------------
RedfishReferenceTool.py is a python3 tool that checks for 
valid reference URLs in CSDL xml files.

cd ~/DMTF-ConformanceTests/Redfish-Reference-Checker
python3 RedfishReferenceTool.py  http://localhost/redfish/v1/\$metadata --nochkcert 2>&1|tee  yourlogname

---------------------------
The Redfish Service Validator is a python3 tool for checking conformance of any 
"device" with a Redfish service interface against Redfish CSDL schema.
Unfortunately you have to have a local directory of schemas pointed to by
the --schemadir option. You can download the schemas with the getSchemas.py utility.

cd ~/DMTF-ConformanceTests/Redfish-Service-Validator
python3 RedfishServiceValidator.py --ip localhost -u root -p calvin --nochkcert --authtype Basic --nooemcheck --schemadir ~/schemas --linklimit 20 2>&1|tee  yourlogname
NOTE: The --nooemcheck option should be used until we solve the Intel Oem problem.

---------------------------
This is a very comprehensive set of tests which will eventually cover all of the Redfish standard
Assertions. It is under constant development.
Unfortunately, this test does not have command line options.
  Edit properties.json.  Fill in the values for LoginName, Password, DnsName

cd ~/DMTF-ConformanceTests/Redfish-Service-Conformance-Check 2>&1|tee  yourlogname
python3 rf_client.py
NOTE: This test runs for a very long time, maybe 30 minutes.
NOTE: The output is extremely long.  About the only
        thing you can do with it is grep for FAIL

```
