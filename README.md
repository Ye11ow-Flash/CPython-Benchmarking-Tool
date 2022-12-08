
# Overarching approach 
## Using AWS

Using AWS the approach relies on using AWS's package, [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html#), to connect to an Amazon Elastic Compute Cloud (AMI). The user can launch different EC2 instances to run various tasks concurrently from the script. This is especially preferred when trying to compare two versions of Python. 

### The steps consists of
1. Launching a benchmark command from the script (CLI). 
2. The CLI will automatically launch an EC2 instance and run a benchmark test on the specified python version.
    1. Set up the virtual environment in the EC2 instance
    2. Gather the repo as needed
3. Run tests
4. Compare the outputs and save the result (maybe in an AWS bucket)
5. Kill or stop the EC2 instance. 


### Open Questions
1. How to deal with more than one benchmark command at a time? I was thinking about using a Queue. 
2. How to deal with an EC2 instance dying prematurely, i.e., in the middle of running some tests? 
    - Consider removing tasks from the queue only when the EC2 instance finished with a given condition. 



## General
A lot of this can be accomplished without using a virtual server. The only issue is that if this is done locally, the user's machine will be directly tied to the tasks. Moreover, benchmark times will vary more widely. Not to mention managing more than one benchmark task at a time.

In any case, further developing the CLI app found here is the best way to go about doing this project. 


# Tools Being Used
The CLI app uses a package called [Typer](https://typer.tiangolo.com/), which is written in Rust and is very fast and easy to use. Even though some scripts have been provided as a starting point, these should be converted to work natively in the CLI.


