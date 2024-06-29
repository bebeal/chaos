# Chaos

TODO: index & make this searchable

TODO: feed through ai to organize this shit and fix potential mistakes

---

Here are some general heuristics to determine when to use each compression method:

Use Git's built-in compression (do nothing special):

For all text files (code, notes, markdown, etc.)
Small binary files that change frequently

Use gzip (single file compression):

Individual large binary files
Files you rarely change but want quick access to
When you need to compress/decompress single files frequently

Use tar.gz (multiple file/directory compression):

Groups of related binaries or tools
Entire directories you want to archive
When you need to preserve directory structure
For collections of files you don't need frequent individual access to

Additional considerations:

Use gzip for files over 1MB if they're not changing often
Use tar.gz when you have more than 3-5 related files to compress
For very large files (100MB+), consider more advanced options like 7zip or xz
