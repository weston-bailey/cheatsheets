# Markdown 

Paragraphs are on the same line. This sentence is still in the same paragraph as the last.

Line breaks need a whole blank line in between paragraphs. Put a whole blank line between pretty much every new markdown thing (headers, code chunks, lists, etc). 

```markdown
Paragraphs are on the same line. This sentence is still in the same paragraph as the last.

Line breaks need a whole blank line in between paragraphs. Put a whole blank line between pretty much every new markdown thing (headers, code chunks, lists, etc).  
```

## Headers

**Headers** are made with `#` hashes

```markdown
# H1

## H2

### H3

#### H4

##### H5

###### H6
```

# H1

## H2

### H3

#### H4

##### H5

###### H6


## Comments

Commented markdown uses HTML comments `<!--  -->` and isn't shown to the reader.

```markdown
<!-- I am a comment! you wouldn't see me! -->
```

# Dividers (Horizontal Rules)

there are three ways to make them. Three underscores `___`, three dashes `---` or three asterisks `***`:


```markdown
___

---

***
```

___

---

***


## Text Styles and Emphasis

**Bold** text is wrapped in two asterisks `**bold**` or two underscores `__bold__` on either side. 

_Italic_ text is wrapped in one asterisk `*italic*` or one underscore `_italic_`.

`Inline code snippets`, or highlights, use backticks ``code``. 

~~Strikethrough~~ uses two tildes on either side `~~strikethrough~~``.

```markdown
**This text will be bold** 

__This will also be bold__ 

*This text will be italic* 

_This will also be italic_ 

`code snippet`

~~This text will be crossed out.~~ 

_You **can** `combine` ~~them~~_

### _And **they** ~~work~~ in `headers`!_
```

**This text will be bold** 

__This will also be bold__ 

*This text will be italic* 

_This will also be italic_ 

`code snippet`

~~This text will be crossed out.~~ 

_You **can** `combine` ~~them~~_

### _And **they** ~~work~~ in `headers`!_

## Lists

You can make unordered lists with asterisks `*` hyphens `-` and plus signs `+` (all interchangeable!). You can also make ordered lists with the number followed by a period `1.`. If you find your lists are bugging out (one list followed by another), giving an extra blank line between them usually fixes it.

```markdown
* asterisk
* asterisk
- hyphen 
- hyphen
+ plus
+ plus

1. one
1. one
```

* asterisk
* asterisk
- hyphen 
- hyphen
+ plus
+ plus


1. one
1. one

Todo lists are started with square brackets after `[]` the list symbol: `- []` and checked off with an `x`: `- [x]` (some markdown versions don't support making done lists look extra cool)

```markdown
- [] need to do
- [] need to do
- [x] nailed it so done
```

- [] need to do
- [] need to do
- [x] nailed it so done

You can indent lists to make sub-lists but ordered lists and unordered lists need to be on different indentation levels! (*i.e. you can't have an unordered list turn into an ordered list halfway through)

```markdown
* asterisk
* asterisk
  - hyphen 
  - hyphen
  + plus
  + plus
1. one
1. one
  - [] need to do
  - [] need to do
  - [x] nailed it so done
```

* asterisk
* asterisk
  - hyphen 
  - hyphen
+ plus
+ plus
  1. one
  1. one
- [] need to do
- [] need to do
- [x] nailed it so done

## Blockquotes

**Blockquotes** start with a wokka `>`  (greater than? less than? what is this thing called...). Subsequent lines that start with a blockquote will be grouped, even with a space between lines.

```markdown
> blockquote

> blockquote
```

> blockquote

> blockquote

This will break without the empty line:

```markdown
> blockquote
> blockquote
```

> blockquote
> blockquote

If you want to combine lists and block quotes, you can just use a wokka `>` on the first item in the list:

```markdown
> * blockquote
* blockquote
* blockquote
  1. ordered list
  2. ordered list
    * [] todos
    * [] todos
```

> * blockquote
* blockquote
* blockquote
  1. ordered list
  2. ordered list
    * [] todos
    * [] todos


```
let generic_demo = {
  code: block
}
```

## Code blocks

Open and close code blocks with three backticks **\`\`\`**. You can have a plaintext code block or specify the language for syntax highlighting after the opening backticks: **\`\`\`javascript**.

<div>
``` 
<br />
plain text
<br />
```
<br />

```python
<br />
def python_code_chunk():
<br />
  return 'syntax highlighting'
<br />
```
<br />

```javascript
<br />
function makeCodePretty() {
<br />
  return 'all the pretty colors'
<br />
}
<br />
```
<br />
</div>

```
plain text code
```

```python
def python_code_chunk():
  return 'syntax highlighting'
```

```javascript
function makeCodePretty() {
  return 'all the pretty colors'
}
```

## Links & Images

```markdown
[title](https://www.example.com)

![alt text](image.jpg)
```

[title](https://www.example.com)

![alt text](image.jpg)

## Tables


```markdown
| Syntax | Description |
| ------ | ----------- |
| Header | Title |
| Paragraph | Text |
| **Bold** | *Italalic* | `code` |
```


| Syntax | Description |
| ------ | ----------- |
| Header | Title |
| Paragraph | Text |
| **Bold** | *Italalic* | `code` | 

## Escaping Characters:

You can escape markdown formatting with a forward slash before the character: `\`.

```markdown
hey, look two backticks \`\` 
hello asterisks \*hello\*
```

hey, look two backticks \`\`

hello asterisks \*hello\*

## HTML

Oh yea, you can do straight-up HTML if you need to.

```markdown
<div>
 Markdown here will not be **parsed**
 </div>
```

<div>
 Markdown here will not be **parsed**
 </div>

 the details html is super useful for spoiler type things:

 ```markdown
<details>
  <summary>Exciting! What if I click on this?</summary>

    Hello there!

</details>
```


<details>
  <summary>Exciting! What if I click on this?</summary>

    Hello there!

</details>
