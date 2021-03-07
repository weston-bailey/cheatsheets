# CSS: Cascading Style Sheets

CSS rules use selectors to style HTML elements, by providing property: value; pairs.
The more specific the rules take precednce, so ids override classes.

```css
selector {
  property_1: value_1;
  property_2: value_2;
}
```

CSS can be added in the head between `<style>` tags or linked in an external stylesheet.

```html
  <head>
    <!-- styling with scripts tags -->
    <style>
      body {
        background: black;
      }
    </style>
    <!-- linking a stylesheet, specify relationship and href -->
    <link rel="stylesheet" href="./css/styles.css" />
    <title>Intro to CSS</title>
  </head>
```


Basic selectors targeting all, classes, ids, elements and attributes:

```css
* {
  /* selects all */
}

.class_selector {
  /* class selector */
}

#id_selector {
  /* id selector */
}

div {
  /* element selector */
}

[attr] {
  /* attribute selector */
}

element.class {
  /* selects elements with a class */
}

.class1.class2 {
  /* selects both classes */
}

.class1 .class2 {
  /* selects class2s that are a child of class1 */
}

element1, element2 {
  /* selects all of both elements */
}

element1 element2 {
  /* selects all element2s that are inside of an element1  */
}

element[attr] {
  /* select element with atrribute */
}

```
Attribute Selectors: 

Syntax | Definition
|------|-----------|
[attr] | selects by attribute
[attr=value] | selects an attribute with exactly a value
[attr~=value] | selects an attribute with a ' value ' with whitespace on both sides
[attr\|=value] | selects an attribute with exactly a value or 'value-' (followed by a hyphen)
[attr^=value] | selects an attribute that starts with value
[attr$=value] | selects an attribute that ends with value
[atttr*=value] | selects an attribute that contains at least on instance of value
[attr operator value i] | selects with case insensitivity
[attr operator value s] | selects with case sensitivity
```










