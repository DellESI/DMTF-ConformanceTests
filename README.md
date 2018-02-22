# DMTF-ConformanceTests
Latest Known Validated Set of Conformance Tests
```
This applies to the dmtftest user on rmdev.

1) The DMTF latest DMTF repositories are probably already
    in the home directory. If in doubt run ./download
    It will also ask if you want to download rackmanager-tools

2) If you want to or need to run tests against the 
    simulator, you can start it with ./startSim

3) Some of the tests do require a local schemas directory.
    To get a local copy:
         ./getSchemas.py (it will ask where to put the schemas)

NOTE: maybe you would rather run all of this from your 
       home dir. If so, from your home dir:
        mkdir <somedir>
        cd <somedir>
        scp -r dmtftest@localhost:. .
        passwd dmtftest
     

Here are SOME SAMPLES of running tests.

1)Every command has a suggested place to save stdout.
  You probably want to customize.
2)Most commands specify the DUT as localhost.
  You may want to change that.
3)All the commands have -h option for full set of options.
  In the samples below are the options that I use.

---------------------------
cd ~/DMTF-ConformanceTests/Redfish-Mockup-Creator
rm -rf ~/mockup-sim-user
python3 redfishMockupCreate.py -T -H -r localhost -u root -p calvin -S -D ~/mockup-sim-user > ~/sim-user-out 
NOTE: This puts the mockup in the home directory.

---------------------------
cd ~/DMTF-ConformanceTests/Redfish-JsonSchema-ResponseValidator
python3 Redfish-JsonSchema-ResponseValidator.py -S -m ~/mockup-sim-user
NOTE: the -S means validate against DMTF's online schemas,
        so you have to be on the internet (which rmdev is).
      alternatively you could point to local schemas with -s.

---------------------------
cd ~/DMTF-ConformanceTests/Redfish-Reference-Checker
python3 RedfishReferenceTool.py  http://localhost/redfish/v1/\$metadata --nochkcert

---------------------------
cd ~/DMTF-ConformanceTests/Redfish-Service-Validator
python3 RedfishServiceValidator.py --ip localhost -u root -p calvin --nochkcert --authtype Basic --schemadir ~/schemas --linklimit 20
NOTE: This requires local schema directory. See instruction above.

---------------------------
cd ~/DMTF-ConformanceTests/Redfish-Service-Conformance-Check
python3 rf_client.py
NOTE: Unfortunately, this test does not have command line options.
       Edit properties.json.
         Fill in the values for LoginName, Password, DnsName
NOTE: This test runs for a very long time, maybe 30 minutes.
NOTE: The output is extremely long.  About the only
        thing you can do with it is grep for FAIL

```
