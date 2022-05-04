LaTeX

## Table:

```latex
\begin{tabular}{ |c|c|c| } 
 cell1 & cell2 & cell3 \\ 
 cell4 & cell5 & cell6 \\  
 cell7 & cell8 & cell9    
\end{tabular}
```

The `tabular` environment is the default LaTeX method to create tables. You must specify a parameter to this environment; here we use { |c|c|c| }  which tells LaTeX that there are three columns, separated by vertical lines `|`, and the text inside each one of them must be centred.  `c` center, `r` right, `l` left.

`\hline`:
This will insert a horizontal line on top of the table and at the bottom too. There is no restriction on the number of times you can use \hline.

`cell1 & cell2 & cell3 \\`:
Each `&` is a cell separator and the double-backslash `\\` sets the end of this row.



