Flux Workflow Examples
----------------------

:doc:`Job Submit CLI <job-submit-cli/README>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launch a flux instance and schedule/launch compute and io-forwarding
jobs on separate nodes using the CLI

:doc:`Job Submit API <job-submit-api/README>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Schedule/launch compute and io-forwarding jobs on separate nodes using
the Python bindings

:doc:`Python Job Submit/Wait <job-submit-wait/README>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Submit jobs and wait for them to complete using the Flux Python bindings

:doc:`Python Asynchronous Bulk Job Submission <async-bulk-job-submit/README>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Asynchronously submit jobspec files from a directory and wait for them
to complete in any order

:doc:`Using Flux Job Status and Control API <job-status-control/README>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Submit job bundles and wait until all jobs complete

:doc:`Use Events <synchronize-events/README>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use events to synchronize compute and io-forwarding jobs running on
separate nodes

:doc:`Simple KVS Python Binding Example <kvs-python-bindings/README>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use KVS Python interfaces to store user data into KVS

:doc:`Job Ensemble Submitted with a New Flux Instance <job-ensemble/README>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Submit job bundles, print live job events, and exit when all jobs are
complete

:doc:`Hierarchical Launching <hierarchical-launching/README>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launch a large number of sleep 0 jobs

:doc:`Use a Flux Comms Module <comms-module/README>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use a Flux Comms Module to communicate with job elements

:doc:`A Data Conduit Strategy <data-conduit/README>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Attach to a job that receives OS time data from compute jobs

.. toctree::
   :hidden:

   job-submit-cli/README
   job-submit-api/README
   job-submit-wait/README
   async-bulk-job-submit/README
   job-status-control/README
   synchronize-events/README
   kvs-python-bindings/README
   job-ensemble/README
   hierarchical-launching/README
   comms-module/README
   data-conduit/README
