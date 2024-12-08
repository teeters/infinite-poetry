## About

The Free Infinite Poetry Generator is a Python application that uses ChatGPT to generate poems by free-associating from a list of words supplied by the user. 

Unbenknownst to the user, two more random words will be omitted from the poem every time a new poem is generated. The image specified in environment variable FORCED_IMAGE will be injected into the poem no matter what.

To make the program work, you will need to run
`export OPENAI_KEY="<secret key>"`
