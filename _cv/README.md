# CV source

`cv.html` is the source for `/Gaurav-Mishra-CV.pdf`. This folder starts with `_`, so GitHub Pages does not publish it.

To rebuild after editing `cv.html` (needs Node and Playwright):

    node _cv/build-pdf.js "$PWD/_cv/cv.html" "$PWD/Gaurav-Mishra-CV.pdf"
