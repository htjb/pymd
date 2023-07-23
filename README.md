## Python MD interpreter

Building my own markdown interpreter. MD is first interpreted into html
and then the html is converted into a PDF.

Currently implemented **bold** fonts, *italics* and <h1>h1 headers</h1>.

Requires [pdfkit](https://pypi.org/project/pdfkit/) to run.

Can run the interpreter on the example file with the following

```bash
python interpreter.py example.md
```
and it will output an example.pdf.