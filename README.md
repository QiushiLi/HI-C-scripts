I am working with a file that contains sequence records and need some assistance extracting specific information. Here are the details:

File Structure:

Lines a to b: These lines contain sequence records with three columns:
Column 1: Sequence ID
Column 2: Sequential code
Column 3: Sequence length
Lines c to end: These lines contain sequential codes (sometimes with a minus sign in front) separated by spaces or line feeds (LF).
Task:

Extract each sequential code from line c to the end of the file.
Find the corresponding sequence ID for each sequential code.
Store the sequence IDs in a separate file.
