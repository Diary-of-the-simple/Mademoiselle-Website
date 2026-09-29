# Obsidian + LaTeX Cheat Sheet

- ## OBSIDIAN KEYBOARD SHORTCUTS
  - Bold: `Ctrl + B`
  - Italic: `Ctrl + I`
  - Insert link: `Ctrl + K`
  - Undo: `Ctrl + Z`
  - Redo: `Ctrl + Y`
  - Find: `Ctrl + F`
  - Replace: `Ctrl + H`
  - Select all: `Ctrl + A`
  - Command palette: `Ctrl + P`
  - Quick switcher: `Ctrl + O`
  - New note: `Ctrl + N`
  - Search vault: `Ctrl + Shift + F`
  - Close tab: `Ctrl + W`
  - Reopen closed tab: `Ctrl + Shift + T`
  - Next tab: `Ctrl + Tab`
  - Previous tab: `Ctrl + Shift + Tab`
  - Settings: `Ctrl + ,`
  - Note: Obsidian shortcuts can be changed under Settings → Hotkeys.

- ## HEADINGS
  - Heading 1: `# Heading`
  - Heading 2: `## Heading`
  - Heading 3: `### Heading`
  - Heading 4: `#### Heading`
  - Heading 5: `##### Heading`
  - Heading 6: `###### Heading`

- ## TEXT FORMATTING
  - Bold: `**text**`
  - Italic: `*text*`
  - Bold + italic: `***text***`
  - Strikethrough: `~~text~~`
  - Highlight: `==text==`
  - Inline code: `` `code` ``
  - Underline: `<u>text</u>`

- ## PARAGRAPHS
  - New paragraph: Leave one blank line between paragraphs.
  - Line break: Add two spaces at the end of a line.
  - HTML line break: `<br>`

- ## UNORDERED LISTS
  - Basic: `- Item`
  - Nested: `- Item` → `  - Nested item`
  - Further nested: `- Item` → `  - Nested` → `    - Further nested`

- ## ORDERED LISTS
  - Basic: `1. Item`
  - Second item: `2. Item`
  - Nested: `1. Item` → `   1. Nested item`

- ## CHECKBOXES
  - Unchecked: `- [ ] Task`
  - Checked: `- [x] Task`
  - Example: `- [ ] Learn Python`
  - Example: `- [x] Install Obsidian`

- ## LINKS
  - External link: `[Google](https://google.com)`
  - Internal note: `[[Note Name]]`
  - Internal note with custom text: `[[Note Name|Display Text]]`
  - Link to heading: `[[Note Name#Heading]]`
  - Link to block: `[[Note Name#^block-id]]`

- ## IMAGES
  - Local image: `![[image.png]]`
  - Image from URL: `![Alt text](https://example.com/image.png)`
  - Image width: `![[image.png|300]]`
  - Image width × height: `![[image.png|300x200]]`

- ## EMBEDS
  - Embed note: `![[Note Name]]`
  - Embed heading: `![[Note Name#Heading]]`
  - Embed block: `![[Note Name#^block-id]]`
  - Embed PDF: `![[document.pdf]]`
  - Embed PDF page: `![[document.pdf#page=3]]`

- ## BLOCKQUOTES
  - Basic quote: `> Quote`
  - Nested quote: `> Quote` → `>> Nested quote` → `>>> Further nested quote`

- ## HORIZONTAL RULES
  - `---`
  - `***`
  - `___`

- ## CODE
  - Inline code: `` `code` ``
  - Code block specification: Start and end with three backticks.
  - Python block specification: Use `python` immediately after the opening three backticks.
  - JavaScript block specification: Use `javascript` immediately after the opening three backticks.
  - HTML block specification: Use `html` immediately after the opening three backticks.
  - CSS block specification: Use `css` immediately after the opening three backticks.
  - Bash block specification: Use `bash` immediately after the opening three backticks.
  - JSON block specification: Use `json` immediately after the opening three backticks.

- ## TABLES
  - Basic table: `| Name | Age | Role |`
  - Separator: `|---|---|---|`
  - Example row: `| Nma | 20 | Developer |`
  - Left alignment: `|:---|`
  - Center alignment: `|:---:|`
  - Right alignment: `|---:|`

- ## CALLOUTS
  - Note: `> [!note]`
  - Tip: `> [!tip]`
  - Important: `> [!important]`
  - Warning: `> [!warning]`
  - Danger: `> [!danger]`
  - Success: `> [!success]`
  - Failure: `> [!failure]`
  - Question: `> [!question]`
  - Example: `> [!example]`
  - Quote: `> [!quote]`
  - Abstract: `> [!abstract]`
  - Info: `> [!info]`
  - Todo: `> [!todo]`
  - Bug: `> [!bug]`
  - Example callout specification:
    - `> [!note]`
    - `> Content goes here.`
  - Collapsed callout specification: Add `-` after the callout type.
  - Collapsed example: `> [!note]-`
  - Expanded callout specification: Add `+` after the callout type.
  - Expanded example: `> [!note]+`

- ## FOOTNOTES
  - Footnote reference: `Sentence.[^1]`
  - Footnote definition: `[^1]: Footnote text`
  - Named footnote: `Sentence.[^important]`
  - Named definition: `[^important]: Important information.`

- ## COMMENTS
  - Single-line comment: `%%hidden text%%`
  - Multiline comment specification: Start and end with `%%`.
  - Multiline example: `%% hidden text %%`

- ## TAGS
  - Tag: `#programming`
  - Multiple tags: `#programming #python #javascript`
  - Nested tag: `#programming/python`

- ## PROPERTIES
  - Properties are placed at the beginning of a note between `---`.
  - Title property: `title: My Note`
  - Date property: `date: 2026-09-26`
  - Tags property: `tags: [python, programming]`
  - Aliases property: `aliases: [Python Notes]`
  - Status property: `status: learning`
  - Example property structure:
    - `---`
    - `title: My Note`
    - `tags:`
    - `  - programming`
    - `  - python`
    - `status: learning`
    - `---`

- ## ALIASES
  - Alias specification: Add `aliases:` inside properties.
  - Example: `aliases: [Python Notes, Python Reference]`
  - Link using alias: `[[Python Notes]]`

- ## HTML
  - Line break: `<br>`
  - Underline: `<u>text</u>`
  - Superscript: `<sup>2</sup>`
  - Subscript: `<sub>2</sub>`
  - Center text: `<center>text</center>`

- ## LATEX BASICS
  - Inline mathematics specification: Surround mathematics with one `$` on each side.
  - Inline example: `$x^2$`
  - Display mathematics specification: Surround mathematics with `$$` on separate lines.
  - Display example: `$$ x^2 $$`
  - Important: Obsidian renders LaTeX using MathJax. You do not need to install LaTeX separately for normal Obsidian math.

- ## LATEX SUPERSCRIPTS
  - Single character: `x^2`
  - Multiple characters: `x^{123}`
  - Expression: `e^{x+1}`
  - Example: `a^{2n}`

- ## LATEX SUBSCRIPTS
  - Single character: `x_1`
  - Multiple characters: `x_{123}`
  - Expression: `x_{n+1}`
  - Example: `a_{ij}`

- ## LATEX FRACTIONS
  - Basic fraction: `\frac{a}{b}`
  - Example: `\frac{x+1}{x-2}`
  - Nested fraction: `\frac{\frac{a}{b}}{c}`

- ## LATEX ROOTS
  - Square root: `\sqrt{x}`
  - Nth root: `\sqrt[n]{x}`
  - Example: `\sqrt{x^2+y^2}`

- ## LATEX BRACKETS
  - Parentheses: `(x)`
  - Automatically sized parentheses: `\left( x \right)`
  - Square brackets: `\left[ x \right]`
  - Curly brackets: `\left\{ x \right\}`
  - Absolute value: `\left|x\right|`
  - Norm: `\left\|x\right\|`

- ## LATEX BASIC OPERATORS
  - Plus: `+`
  - Minus: `-`
  - Multiply: `\times`
  - Divide: `\div`
  - Plus or minus: `\pm`
  - Minus or plus: `\mp`
  - Equal: `=`
  - Not equal: `\neq`
  - Approximately equal: `\approx`
  - Less than: `<`
  - Greater than: `>`
  - Less than or equal: `\leq`
  - Greater than or equal: `\geq`
  - Proportional: `\propto`
  - Equivalent: `\equiv`
  - Similar: `\sim`
  - Therefore: `\therefore`
  - Because: `\because`

- ## LATEX GREEK LETTERS
  - Alpha: `\alpha`
  - Beta: `\beta`
  - Gamma: `\gamma`
  - Delta: `\delta`
  - Epsilon: `\epsilon`
  - Variant epsilon: `\varepsilon`
  - Zeta: `\zeta`
  - Eta: `\eta`
  - Theta: `\theta`
  - Variant theta: `\vartheta`
  - Iota: `\iota`
  - Kappa: `\kappa`
  - Lambda: `\lambda`
  - Mu: `\mu`
  - Nu: `\nu`
  - Xi: `\xi`
  - Pi: `\pi`
  - Variant pi: `\varpi`
  - Rho: `\rho`
  - Variant rho: `\varrho`
  - Sigma: `\sigma`
  - Variant sigma: `\varsigma`
  - Tau: `\tau`
  - Upsilon: `\upsilon`
  - Phi: `\phi`
  - Variant phi: `\varphi`
  - Chi: `\chi`
  - Psi: `\psi`
  - Omega: `\omega`
  - Capital Gamma: `\Gamma`
  - Capital Delta: `\Delta`
  - Capital Theta: `\Theta`
  - Capital Lambda: `\Lambda`
  - Capital Xi: `\Xi`
  - Capital Pi: `\Pi`
  - Capital Sigma: `\Sigma`
  - Capital Upsilon: `\Upsilon`
  - Capital Phi: `\Phi`
  - Capital Psi: `\Psi`
  - Capital Omega: `\Omega`

- ## LATEX SUMMATION
  - Basic summation: `\sum`
  - Summation with limits: `\sum_{i=1}^{n}`
  - Example: `\sum_{i=1}^{n}x_i`
  - Example with formula: `\sum_{i=1}^{n}i=\frac{n(n+1)}{2}`

- ## LATEX PRODUCT
  - Basic product: `\prod`
  - Product with limits: `\prod_{i=1}^{n}`
  - Example: `\prod_{i=1}^{n}x_i`

- ## LATEX INTEGRALS
  - Integral: `\int`
  - Definite integral: `\int_a^b`
  - Integral with function: `\int_a^b f(x)\,dx`
  - Double integral: `\iint`
  - Triple integral: `\iiint`
  - Contour integral: `\oint`

- ## LATEX LIMITS
  - Limit: `\lim`
  - Limit with variable: `\lim_{x\to a}`
  - Limit at infinity: `\lim_{x\to\infty}`
  - Example: `\lim_{x\to0}\frac{\sin x}{x}`

- ## LATEX DERIVATIVES
  - First derivative: `\frac{dy}{dx}`
  - Second derivative: `\frac{d^2y}{dx^2}`
  - Nth derivative: `\frac{d^ny}{dx^n}`
  - Partial derivative: `\frac{\partial f}{\partial x}`
  - Second partial derivative: `\frac{\partial^2f}{\partial x^2}`

- ## LATEX DIFFERENTIAL EQUATIONS
  - Basic differential equation: `\frac{dy}{dx}=f(x,y)`
  - Example: `\frac{dy}{dx}+y=0`
  - Second-order example: `\frac{d^2y}{dx^2}+y=0`

- ## LATEX VECTORS
  - Vector arrow: `\vec{x}`
  - Bold vector: `\mathbf{x}`
  - Unit vector: `\hat{x}`
  - Vector with components: `\vec{v}=\begin{bmatrix}v_1\\v_2\\v_3\end{bmatrix}`

- ## LATEX VECTOR CALCULUS
  - Gradient: `\nabla f`
  - Divergence: `\nabla\cdot\mathbf{F}`
  - Curl: `\nabla\times\mathbf{F}`
  - Laplacian: `\nabla^2f`

- ## LATEX MATRICES
  - Matrix specification: Use `\begin{matrix}` and `\end{matrix}`.
  - Basic matrix: `\begin{matrix} 1 & 2 \\ 3 & 4 \end{matrix}`
  - Parentheses matrix: `\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}`
  - Square bracket matrix: `\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}`
  - Curly bracket matrix: `\begin{Bmatrix} 1 & 2 \\ 3 & 4 \end{Bmatrix}`
  - Vertical determinant: `\begin{vmatrix} a & b \\ c & d \end{vmatrix}`
  - Matrix column separator: `&`
  - Matrix row separator: `\\`

- ## LATEX PIECEWISE FUNCTIONS
  - Piecewise specification: Use `\begin{cases}` and `\end{cases}`.
  - Example: `f(x)=\begin{cases}x^2 & x>0\\0 & x=0\\-x^2 & x<0\end{cases}`

- ## LATEX ALIGNED EQUATIONS
  - Alignment specification: Use `\begin{aligned}` and `\end{aligned}`.
  - Alignment point: `&`
  - New equation line: `\\`
  - Example: `\begin{aligned}x&=a+b\\&=c\end{aligned}`

- ## LATEX TEXT
  - Text inside mathematics: `\text{word}`
  - Example: `x>0\quad\text{if }x>0`
  - Roman operator text: `\operatorname{Var}(X)`
  - Common operator: `\operatorname{tr}(A)`

- ## LATEX SPACING
  - Small space: `\,`
  - Medium space: `\:`
  - Large space: `\;`
  - Quad space: `\quad`
  - Double quad space: `\qquad`

- ## LATEX FUNCTIONS
  - Sine: `\sin`
  - Cosine: `\cos`
  - Tangent: `\tan`
  - Cotangent: `\cot`
  - Secant: `\sec`
  - Cosecant: `\csc`
  - Arcsine: `\arcsin`
  - Arccosine: `\arccos`
  - Arctangent: `\arctan`
  - Logarithm: `\log`
  - Natural logarithm: `\ln`
  - Exponential: `\exp`

- ## LATEX SET THEORY
  - Element of: `\in`
  - Not element of: `\notin`
  - Subset: `\subset`
  - Subset or equal: `\subseteq`
  - Superset: `\supset`
  - Superset or equal: `\supseteq`
  - Union: `\cup`
  - Intersection: `\cap`
  - Empty set: `\emptyset`
  - Set difference: `\setminus`

- ## LATEX NUMBER SETS
  - Natural numbers: `\mathbb{N}`
  - Integers: `\mathbb{Z}`
  - Rational numbers: `\mathbb{Q}`
  - Real numbers: `\mathbb{R}`
  - Complex numbers: `\mathbb{C}`
  - Example: `x\in\mathbb{R}`

- ## LATEX LOGIC
  - And: `\land`
  - Or: `\lor`
  - Not: `\neg`
  - Implies: `\implies`
  - If and only if: `\iff`
  - For all: `\forall`
  - There exists: `\exists`
  - There does not exist: `\nexists`

- ## LATEX ARROWS
  - Right arrow: `\rightarrow`
  - Left arrow: `\leftarrow`
  - Left-right arrow: `\leftrightarrow`
  - Long right arrow: `\longrightarrow`
  - Double right arrow: `\Rightarrow`
  - Double left arrow: `\Leftarrow`
  - Double left-right arrow: `\Leftrightarrow`
  - Maps to: `\mapsto`

- ## LATEX ACCENTS
  - Hat: `\hat{x}`
  - Wide hat: `\widehat{ABC}`
  - Bar: `\bar{x}`
  - Overline: `\overline{AB}`
  - Underline: `\underline{x}`
  - Dot: `\dot{x}`
  - Double dot: `\ddot{x}`

- ## LATEX PROBABILITY
  - Probability: `P(A)`
  - Conditional probability: `P(A\mid B)`
  - Expected value: `E[X]`
  - Variance: `\operatorname{Var}(X)`
  - Covariance: `\operatorname{Cov}(X,Y)`

- ## LATEX STATISTICS
  - Mean: `\bar{x}`
  - Standard deviation: `\sigma`
  - Variance: `\sigma^2`
  - Sample mean: `\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i`

- ## LATEX LINEAR ALGEBRA
  - Matrix multiplication: `AB`
  - Transpose: `A^T`
  - Inverse: `A^{-1}`
  - Determinant: `\det(A)`
  - Trace: `\operatorname{tr}(A)`
  - Eigenvalue equation: `Av=\lambda v`
  - Characteristic equation: `\det(A-\lambda I)=0`

- ## LATEX NUMERICAL METHODS
  - Newton-Raphson: `x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}`
  - Bisection midpoint: `c=\frac{a+b}{2}`
  - Secant method: `x_{n+1}=x_n-f(x_n)\frac{x_n-x_{n-1}}{f(x_n)-f(x_{n-1})}`
  - Trapezoidal rule: `\int_a^b f(x)\,dx\approx\frac{b-a}{2}[f(a)+f(b)]`
  - Composite trapezoidal rule: `\int_a^b f(x)\,dx\approx\frac{h}{2}[f(x_0)+2\sum_{i=1}^{n-1}f(x_i)+f(x_n)]`
  - Simpson's 1/3 rule: `\int_a^b f(x)\,dx\approx\frac{h}{3}[f(x_0)+4f(x_1)+f(x_2)]`
  - Lagrange interpolation: `P(x)=\sum_{i=0}^{n}y_i\prod_{\substack{j=0\\j\neq i}}^n\frac{x-x_j}{x_i-x_j}`

- ## LATEX PHYSICS
  - Velocity: `v=\frac{dx}{dt}`
  - Acceleration: `a=\frac{dv}{dt}`
  - Newton's second law: `F=ma`
  - Kinetic energy: `KE=\frac{1}{2}mv^2`
  - Potential energy: `PE=mgh`
  - Momentum: `p=mv`
  - Einstein's equation: `E=mc^2`

- ## LATEX CHEMISTRY
  - Water: `H_2O`
  - Sodium ion: `Na^+`
  - Chloride ion: `Cl^-`
  - Chemical reaction: `2H_2+O_2\rightarrow2H_2O`

- ## LATEX SPECIAL SYMBOLS
  - Infinity: `\infty`
  - Partial derivative: `\partial`
  - Nabla: `\nabla`
  - Delta: `\Delta`
  - Square root: `\sqrt{}`
  - Plus/minus: `\pm`
  - Multiplication: `\times`
  - Division: `\div`
  - Not equal: `\neq`
  - Approximately equal: `\approx`
  - Less/equal: `\leq`
  - Greater/equal: `\geq`
  - Element: `\in`
  - Not element: `\notin`
  - For all: `\forall`
  - Exists: `\exists`
  - Sum: `\sum`
  - Product: `\prod`
  - Integral: `\int`
  - Contour integral: `\oint`
  - Union: `\cup`
  - Intersection: `\cap`
  - Right arrow: `\rightarrow`
  - Left arrow: `\leftarrow`
  - Implies: `\Rightarrow`
  - Equivalent: `\Leftrightarrow`
  - Proportional: `\propto`
  - Therefore: `\therefore`
  - Because: `\because`

- ## LATEX ROW AND COLUMN RULES
  - In matrices, `&` separates columns.
  - In matrices, `\\` starts a new row.
  - In aligned equations, `&` determines alignment.
  - In aligned equations, `\\` starts a new equation.
  - Example matrix: `\begin{bmatrix}a&b\\c&d\end{bmatrix}`

- ## LATEX QUICK REFERENCE
  - Inline math specification: `$formula$`
  - Display math specification: `$$ formula $$`
  - Power: `x^2`
  - Subscript: `x_1`
  - Multiple-character power: `x^{abc}`
  - Multiple-character subscript: `x_{abc}`
  - Fraction: `\frac{a}{b}`
  - Root: `\sqrt{x}`
  - Nth root: `\sqrt[n]{x}`
  - Sum: `\sum_{i=1}^{n}`
  - Product: `\prod_{i=1}^{n}`
  - Integral: `\int_a^b`
  - Limit: `\lim_{x\to a}`
  - Derivative: `\frac{dy}{dx}`
  - Partial derivative: `\frac{\partial f}{\partial x}`
  - Matrix: `\begin{bmatrix}...\end{bmatrix}`
  - Cases: `\begin{cases}...\end{cases}`
  - Alignment: `\begin{aligned}...\end{aligned}`

- ## MOST IMPORTANT OBSIDIAN SYNTAX TO MEMORIZE
  - Heading: `#`
  - Bold: `**text**`
  - Italic: `*text*`
  - Highlight: `==text==`
  - Strikethrough: `~~text~~`
  - Internal link: `[[Note]]`
  - Embed: `![[Note]]`
  - External link: `[Text](URL)`
  - Checkbox: `- [ ]`
  - Completed checkbox: `- [x]`
  - Quote: `>`
  - Callout: `> [!note]`
  - Tag: `#tag`
  - Inline code: `` `code` ``
  - Inline math: `$x$`
  - Display math: `$$x$$`

- ## MOST IMPORTANT LATEX COMMANDS TO MEMORIZE
  - Power: `^`
  - Subscript: `_`
  - Fraction: `\frac{}{}`
  - Root: `\sqrt{}`
  - Sum: `\sum`
  - Integral: `\int`
  - Limit: `\lim`
  - Derivative: `\frac{dy}{dx}`
  - Partial derivative: `\partial`
  - Infinity: `\infty`
  - Alpha: `\alpha`
  - Beta: `\beta`
  - Gamma: `\gamma`
  - Theta: `\theta`
  - Lambda: `\lambda`
  - Pi: `\pi`
  - Sigma: `\sigma`
  - Omega: `\omega`
  - Less/equal: `\leq`
  - Greater/equal: `\geq`
  - Not equal: `\neq`
  - Approximately: `\approx`
  - Real numbers: `\mathbb{R}`
  - Natural numbers: `\mathbb{N}`
  - Integers: `\mathbb{Z}`
  - Complex numbers: `\mathbb{C}`
  - Matrix: `\begin{bmatrix}...\end{bmatrix}`
  - Aligned equations: `\begin{aligned}...\end{aligned}`
  - Piecewise function: `\begin{cases}...\end{cases}`

- ## COMPLETE EXAMPLE
  - Note title: `Newton-Raphson Method`
  - Formula: `$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$`
  - Display formula specification: Put the formula between `$$` on separate lines.
  - Example display formula: `x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}`
  - Algorithm:
    - `1. Choose an initial guess x_0.`
    - `2. Calculate f(x_0).`
    - `3. Calculate f'(x_0).`
    - `4. Apply the Newton-Raphson formula.`
    - `5. Repeat until the desired accuracy is reached.`
  - Related note: `[[Numerical Methods]]`
  - Related note: `[[Bisection Method]]`
  - Related note: `[[Secant Method]]`
  - Related note: `[[Interpolation]]`

- ## END

