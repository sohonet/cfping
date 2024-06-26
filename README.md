cfping
======

Test the performance and availability of the Rackspace cloudfiles or Openstack swift service.


Example
-------

    $ cfping
    Pinging storage (sending request every 1 seconds with 81.0 bytes ):
        seq. #       auth    connect  container      write       read     delete      total
             1      0.100      0.061      0.041      0.286      0.009      0.034      0.532
             2      0.068      0.059      0.031      0.168      0.010      0.014      0.351
             3      0.067      0.058      0.027      0.085      0.009      0.013      0.260
             4      0.066      0.059      0.012      0.090      0.009      0.014      0.251
             5      0.066      0.061      0.044      0.052      0.010      0.014      0.247
    ^C
    5 requests


Usage
-----

    usage: cfping [-h] [-u USERNAME] [-k KEY] [-a AUTHURL] [-t TENANT ]
            [-c CONTAINER] [-s] [-i PING_INTERVAL] [-r PING_REPETITIONS]
	    [-t TEST_DATA_SIZE] [-m] [-d]
            [--graphite-root-metric-path GRAPHITE_ROOT_METRIC_PATH]
            [--carbon-server-ip CARBON_SERVER_IP]
            [--carbon-port CARBON_PORT]

            Test the performance and availability of the Rackspace cloudfiles or Openstack swift service.

            optional arguments:
            -h, --help            show this help message and exit
            -u USERNAME, --username USERNAME
                      Storage service username (default: OS_USERNAME)
            -t TENANTNAME, --tenantname TENANTNAME
                        Storage service username (default: OS_TENANT_NAME)	
            -k KEY, --key KEY     Storage service API key (default: OS_PASSWORD)
            -a AUTHURL, --authurl AUTHURL
                      Storage service auth URL (default:
                      https://auth.api.rackspacecloud.com/v1.0)
            -V AUTH_VERSION, --auth_version AUTH_VERSION
                        Storage service auth version (default: 2 if OS_AUTH_VERSION absent
            -c CONTAINER, --container CONTAINER
                      Use the specified container (default: use the first
                      container [index 0])
            -s, --service-net     Use the Rackspace service network (default: use public
                      network)
            -i PING_INTERVAL, --interval PING_INTERVAL
                      Seconds to wait between ping requests (default: 60
                      seconds)
            -r PING_REPETITIONS, --repetitions PING_REPETITIONS
                      Number of repetitions (default: infinite) 
            -T TEST_DATA_SIZE, --test-data-size TEST_DATA_SIZE
                      Test data size in Bytes (default: 81 Bytes)
            -m, --machinereadable
                      Output results with no headers
            -d, --data            Output statistics for the tests, min, max, and average
                      (mean)
            --graphite-root-metric-path GRAPHITE_ROOT_METRIC_PATH
                      The root of the graphite metric path (default:
                      GRAPHITE_ROOT cfping.)
            --carbon-server-ip CARBON_SERVER_IP
                      IPv4 address of the carbon server (default:
                      CARBON_IP)
            --carbon-port CARBON_PORT
                      Carbon server port (default: CARBON_PORT 2003)


Environment
-----------

`cfping` accepts the following environment variables:

* `OS_USERNAME`, the account username. The `-u` option, if provided, takes precedence.
* `OS_PASSWORD`, the account key. The `-k` option, if provided, takes precedence.
* `OS_AUTH_URL`, the authentication endpoint. The `-a` option, if provided, takes precedence.
* `OS_AUTH_VERSION`, the authentication version. Defaults to 2
* `CARBON_PORT`, the port that graphite carbon is listening on.
* `CARBON_SERVER_IP`, the IPv4 address of the server.
* `GRAPHITE_ROOT`, the root of the metric path, cfping.metrics.read

Installation
------------

`cfping` is a Python program and can be installed with `pip` (or `easy_install`):

    $ pip install cfping


Contributing
------------

`cfping` is open-source software and your contributions are welcome.

Open an [issue](https://github.com/claymation/cfping/issues) on GitHub to report a bug or suggest an enhancement,
or better yet, fork the repo and send a [pull request](https://github.com/claymation/cfping/pulls).
