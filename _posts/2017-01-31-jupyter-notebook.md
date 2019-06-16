---
layout: post
title:  "Theming Jupyter Notebooks"
date:   2019-03-16
desc: "Theming Jupyter Notebooks"
keywords: "python, machine learning, jupyter, notebook, deeplearning, code, jupyter notebook"
categories: [python, machine learning, jupyter, notebook, deeplearning, code, jupyter notebook]
tags: [python, machine learning, jupyter, notebook, deeplearning, code, jupyter notebook]
icon: icon-google-developers
---

**Machine learning** is the new trend everywhere. Every developer I meet is into machine learning these days (including me).
You are for sure to stumble upon **Jupyter Notebooks** if you are into machine learning stuff. Basically, **Jupyter Notebooks** are
documents the contain both computer code (_e.g. python_) and rich text elements (_paragraph, equations, figures, links, etc…_). Notebook documents are both human-readable documents containing the analysis description and the results (_figures, tables, etc.._) as well as executable documents. 

**Jupyter Notebooks** has support for over 40 programming languages, including Python, R, Julia, and Scala.

If you are like me then you are never satisfied with out of the box experience on any development environment. I literally spend hours 
tweaking tools, changing fonts, colors and what not. Making the tools/ides look better than the code to be honest. I am writing this guide for Ubuntu/Linux users but this should pretty much help for all platforms. You just have to search for the respective folders. So, let's begin.

## We will start by tweaking the default theme that's provided by jupyter.

- For this you will need to find `.jupyter` folder - Usually located in `home/.jupyter`. Try `ctrl + h` if your files are hidden.
- Then, you need to navigate inside the folder and go inside `custom` folder. Now, all you need to do is change `custom.css` file.
- If you do not like the width of your notebook then you can change it by adding the snippet below in `custom.css` file. Do not change anything else (I am not responsible for the things you break, or just take a back up of your `custom.css` before moving further.).

        .container { 
            width:90% !important; 
        }

- You can also change the fonts. Just replace the font name in the same file and most of all remember to place the font under `fonts` folder
the you will find right beside `custom.css`
- Also, I have no idea what `custom.js` does. 


If you are curious on what styles am I using then here is the full `custom.css` of mine:

    @font-face {
        font-family: "Hasklig";
        font-weight: normal;
        font-style: italic;
        src: local('"Hasklig"'), url('fonts/hasklig.otf') format('opentype');
    }
    @font-face {
    font-family: "Hasklig";
    font-weight: normal;
    font-style: italic;
    src: local('"Hasklig"'), url('fonts/hasklig-italic.otf') format('opentype');
    }

    .container { 
        width:90% !important; 
    }

    div#notebook {
        font-size: 11px;
    }

    div.prompt {
        min-width: 10ex;
    }

    .timing_area {
        font-size: 60% !important;
    }

    .CodeMirror {
        line-height: 1.50em;
        font-size: 12px;
        height: auto;
        background: none;
    }

    .completions select {
        background: white;
        outline: none;
        border: none;
        padding: 0px;
        margin: 0px;
        overflow: auto;
        font-family: monospace;
        font-size: 90%;
        color: #000;
        width: auto;
    }

    <script>
        MathJax.Hub.Config({
            "HTML-CSS": {
                /*preferredFont: "TeX",*/
                /*availableFonts: ["TeX", "STIX"],*/
                styles: {
                    scale: 80,
                    ".MathJax_Display": {
                        "font-size": "80%",
                    }
                }
            }
        });
    </script>
            

By, this time you might wonder on how I got the css selectors name (_Eg: css class names_). For this you need to start **Jupyter Notebook**
and open any `.ipynb` files that you have. `.ipynb` files are basically the iPython files (Interative Python). You can then inspect element
on the page and select the class name of the element that you would like to change. (`ctrl+shift+c` _In case you prefer shortcuts_)


## There is another way too:

Refer this for more: [jupyter-themes](https://github.com/dunovank/jupyter-themes)

Things to do now:

- Install jupyter themes : `pip install jupyterthemes`
- Simply use it by: `jt [commands]`

    
My favorite one is: 
    
> jt -t grade3 -T -N -fs 9 -nfs 9 -tfs 9 -cellw 1200

Here, `-t` means use `grade3` theme, `-T` stands for _Toolbars on_, `-N` stands for _Notebook name on_, `-fs` means use _font size 9_,
`-nfs` means use _notebook font size 9_, `-tfs` means use toolbar _font size 9_ and finally `-cellw` means _use 1200 as the width for the notebook workspace_.

#### You might want to check out the original repository mentioned in the link above to try out different themes and others interesting stuffs.


