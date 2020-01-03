**Flux Workflow Examples**

**_1. [Partitioning Schedule](https://github.com/flux-framework/flux-workflow-examples/tree/master/example1)_**

Launch a flux instance and schedule/launch compute and io-forwarding jobs on
separate nodes using the CLI

**_2. [Use a Direct job.submit RPC](https://github.com/flux-framework/flux-workflow-examples/tree/master/example2)_**

Schedule/launch compute and io-forwarding jobs on separate nodes using the Lua and Python bindings

**_3. [Use Events](https://github.com/flux-framework/flux-workflow-examples/tree/master/example3)_**

Use events to synchronize compute and io-forwarding jobs running on separate
nodes

**_4. [Job Ensemble Submitted with a New Flux Instance](https://github.com/flux-framework/flux-workflow-examples/tree/master/example4)_**

Launch a flux instance and submit one instance of an io-forwarding job and a
large number of compute jobs, each spanning the entire set of the node

**_5. [Use a Flux Comms Module](https://github.com/flux-framework/flux-workflow-examples/tree/master/example5)_**

Use a Flux Comms Module to communicate with job elements

**_6. [Hierarchical Launching](https://github.com/flux-framework/flux-workflow-examples/tree/master/example6)_**

Launch a large number of sleep 0 jobs

**_7. [Using Flux Job Status and Control API](https://github.com/flux-framework/flux-workflow-examples/tree/master/example7)_**

Submit job bundles and wait until all jobs complete

**_8. [Simple KVS Python Binding Example](https://github.com/flux-framework/flux-workflow-examples/tree/master/example9)_**

Use KVS Python interfaces to store user data into KVS

**_9. [A Data Conduit Strategy](https://github.com/flux-framework/flux-workflow-examples/tree/master/example10)_**

Attach to a job that receives OS time data from compute jobs
