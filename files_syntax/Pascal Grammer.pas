!	' |\r|\n|\t|//[^\n]*\n'
;
'\-'
'\+'
'not'
'\('
'\)'
'and'
'mod'
'div'
'/'
'\*'
'or'
'>'
'>='
'='
'<>'
'<='
'<'
','
'\]'
'\['
'do'
'while'
'else'
'then'
'if'
':='
';'
'end'
'begin'
':'
'function'
'procedure'
'real'
'integer'
'\.\.'
'of'
'array'
'var'
'\.'
'program'
'end\.'
'downto'
'to'
'do'
'for'
'id'		
'int'						
'float'	
'string'
'boolean'
;
##

P:
		'program' 'id' output ';' 
		declarations
		subprogram_declaration
		'begin' 
		optional_statment
		'end\.'
		;

output:
		'\(' id_list '\)'
		|;

id_list	:
		'id'
		|id_list ',' 'id'
		;

declarations:
		declarations 'var' id_list ':' type ';'
		|;

type:
		standard_type
		|'array' '\[' 'int' '\.\.' 'int' '\]' 'of' standard_type
		;

standard_type:
		'integer'
		|'real'
		|'string'
		|'boolean'
		;

subprogram_declaration:
		subprogram_declarations subprogram_declaration ';'
		|;

subprogram_declarations:
		supprogram_head declarations compound_statment
		;

supprogram_head:
		'function' 'id' arguments ':' standard_type ';' 
		|'procedure' 'id' arguments ';'
		;

arguments:
		'\(' parameter_list '\)'
		|;

parameter_list:
		id_list ':' type
		|parameter_list ';' id_list ':' type
		;

compound_statment:
		'begin' optional_statment 'end'
		;

optional_statment:
		statment_list
		|;

statment_list:
		statment
		|statment_list ';' optional_statment
		;

statment:
		varible ':=' expr 
		|procedure_statment 
		|compound_statment
		|'if' expr 'then' statment
		|'if' expr 'then' statment 'else' statment
		|'while' expr 'do' statment
		|'for' varible ':=' expr st_for st_for2 'do' statment
		;

st_for:
		'to'
		|'downto'
		;

st_for2:
		'id'
		|'int'
		;

varible:
		'id'
		|'id' '\[' expr '\]'
		;

procedure_statment:
		'id'
		|'id' '\(' expr_list '\)'
		;

expr_list:
		expr
		|expr_list ',' expr
		|;

expr:
		simple_expr
		|simple_expr relop simple_expr
		;

relop:
		'<'
		|'<='
		|'<>'
		|'='
		|'>='
		|'>'
		;

simple_expr:
		term
		|sign term
		|simple_expr addop term
		;

addop:
		'\+'
		|'\-'
		|'or'
		;

term:
		factor
		|term mulop factor
		;

mulop:
		'\*'
		|'/'
		|'div'
		|'mod'
		|'and'
		;

factor:
		'id'
		|'id' '\(' expr_list '\)'
		|'int'
		|'float'
		|'string'
		|'boolean'
		|'\(' expr '\)'
		|'not' factor
		;

sign:
		'\+'
		|'\-'
		;